## Task 1: 理解订单簿，实现限价单数据模型

# **做什么**: 设计一个 `OrderBook` 类，能够接收限价买单和卖单，并按规则组织存储。

# **思考提示**:
# - 买方出价（bid）和卖方要价（ask）分别应该按什么顺序排列？为什么？
# - 当买一价和卖一价之间存在间隙（spread），这个间隙代表什么经济含义？
# - 为什么不能用一个简单的列表来存储订单？什么数据结构更合适？

# **验证**: 你能往订单簿里添加多个买单和卖单，打印出来后买方按价格从高到低排列，卖方按价格从低到高排列。

# 📚 **关键资料**:
# - 搜索「Order Book」和「Limit Order Book」的概念，理解 bid/ask/spread
# - 了解 Python 的 `heapq` 模块或 `sortedcontainers` 库，思考哪个适合做订单簿

# ------------------------- Answer -------------------------#
# Order Book 准则：
# 1. 价格优先
# 2. 时间优先
# 所以一个最小原子必须包含：价格，时间戳
# Order Book 还需要记录量能，所以还需要包含：买卖手
# 所以一个 Order item 需要包含：price / timestamp / quantity
# 还需要记录属于：ask or bid

# [AI 批注] ⚠️ 思考题只回答了一半。题目三个 prompt 你只答了第一条（排序规则）。
# 建议补上另外两条的思考，这是真正构建直觉的地方：
#
# Q2: spread（买一卖一间隙）的经济含义是什么？
#     提示：想想「做市商为什么敢挂双边单？」、「spread 越小说明市场什么状态？」
#     关键词：liquidity cost、市场深度、做市商报价
# Answer: 间隙越小分歧越小？表示市场的活跃程度？spread 越小越活跃？
# [AI 批注] 📝 方向对了一半。"spread 越小 → 市场越活跃"这个结论是对的，但理由不够精确。
#     "分歧越小"不是 spread 的本质——买卖双方永远有分歧，否则就没有交易了。
#     Spread 更准确的含义是：**立即成交的代价（liquidity cost）**。
#     你想想：如果你现在就想买，你必须付 ask 价（比 bid 高）；
#     如果你想卖，你只能拿 bid 价（比 ask 低）。这个差就是你为"立即执行"付的成本。
#     所以 spread 小 → 立即成交的代价低 → 市场流动性好 → 交易活跃。
#     再想一层：谁在赚这个 spread？（关键词：做市商、market maker）
#
# Q3: 为什么不能用简单 list？什么结构更合适？
#     你实际上已经用 SortedDict 回答了，但没把"为什么"写下来。
#     提示：列表在中间插入是 O(n)，按价格查最优档是 O(n)；真实交易所每秒几十万笔，
#     必须 O(log n) 级别。SortedDict 背后是 B-tree 变种，正好符合需求。
#     关键词：time complexity、red-black tree、skip list
# Answer: 如果用 list 不能满足纳秒级别的交易要求，list 的寻址 / 排序 / 插入 等操作都是 O(n) 起，
#         SortedDict 操作都可以直接通过 key 访问访问地址下标，这样更满足交易对时间效率的要求。
# [AI 批注] 📝 结论对但表述有两处不准确：
#     1. list "寻址"（按下标访问）其实是 O(1)，不慢。慢的是"按价格查找" O(n)
#        和"在中间插入/删除" O(n)。区分"按下标访问"和"按值查找"很重要。
#     2. "SortedDict 通过 key 直接访问地址下标"——听起来像 O(1)，
#        实际上 SortedDict 的 key 查找是 O(log n)（内部是平衡树/跳表）。
#        关键对比是：O(log n) vs O(n)，不是 O(1) vs O(n)。
#     试着列一张表：list vs SortedDict 在 insert / delete / find_min / find_by_key
#     四种操作上各自的复杂度。写完你会对"为什么选 SortedDict"有更清晰的理解。

from dataclasses import dataclass, field
from collections import OrderedDict
from enum import Enum
from sortedcontainers import SortedDict

# 在 terminal 打印表格
from tabulate import tabulate

# 自增 ID（有序、便于排查、还能作 tie-breaker）：
from itertools import count
from typing import Iterator

# get timestamp
import time

from itertools import zip_longest

Price = float
Quantity = int
OrderId = int

class Side(Enum):
    BID = "bid"
    ASK = "ask"

@dataclass
class OrderRequest:
    side: Side
    price: Price
    quantity: Quantity

# [AI 批注] ✅ OrderRequest/Order 分离得非常漂亮。
# 外部调用方只给 side/price/quantity，id 和 timestamp 由撮合引擎负责分配 ——
# 这正是真实交易所的契约边界。继承复用字段声明也很 Pythonic。


@dataclass
class Order(OrderRequest):
    id: OrderId
    timestamp: int
    # [AI 批注] ✅ 已修正。timestamp 类型标注改成了 int，和 time.time_ns() 返回值一致。


Book = SortedDict[Price, OrderedDict[OrderId, Order]]
# [AI 批注] ✅ 这个类型别名提炼得特别好。
# 一眼就能看出数据结构的三层语义：
# - 外层 SortedDict：按价格排序（价格优先）
# - 内层 OrderedDict：按插入顺序存储同价位订单（时间优先）
# - value 是 Order：完整订单信息
# 这个别名后面在 print_books_l2 的 format_rows 参数里复用了，语义清晰度+1。


@dataclass
class OrderBook:
    _id_seq: Iterator[int] = field(default_factory= lambda: count(1))
    # [AI 批注] ✅ 已修正。用 field(default_factory=lambda: count(1)) 替换了类属性，
    # 现在每个 OrderBook 实例都有独立的 id 序列。
    # 延伸思考还在：真实交易所里不同交易对的 order id 应不应该共享？留着以后想。

    # 为什么需要加 field(factory=xxx)
    # 因为 Python 里默认值在"定义时"求值一次，不是每次实例化都重新求值。
    # 如果实例化多次，则另一个对象也使用了到了这个值
    # example:
    # a = OrderBook()
    # b = OrderBook()
    # a.bids is b.bids == true
    bids: Book = field(
        # 买单，高价优先，所以按照价格降序
        default_factory=lambda: SortedDict(lambda price: -price)
        )

    # 卖单，低价优先，所以按照价格升序
    asks: Book = field(default_factory=SortedDict)
    # [AI 批注] ✅ 这两个 default_factory 写得完全正确，注释里还解释了 why，很棒。
    # 留意 asks 直接传 SortedDict（类本身）当 factory，比 lambda: SortedDict() 更简洁 ——
    # 因为类对象本身就是 callable。

    # 接受限价单
    def add_order(self, req: OrderRequest) -> Order:
        # [AI 批注] ✅ 已修正。add_order 末尾加了 return order，调用方现在能拿到订单对象了。

        # 提前组装好 Order dict
        order = Order(
            **req.__dict__,
            id = next(self._id_seq),
            timestamp  = time.time_ns()
        )
        # [AI 批注] ✅ 用 **req.__dict__ 解包继承父类字段很干净。
        # 一次性构造好 Order，避免了"先建后补字段"的可变操作。

        # 判断 order 类型，决定归档到哪里
        book = self.bids if order.side == Side.BID else self.asks

        # setdefault(key, default) 的语义：key 存在就返回现有的值，不存在就把 default 存进去并返回。
        book.setdefault(req.price, OrderedDict())[order.id] = order
        # [AI 批注] ✅ 这一行是这段代码的高光。
        # 一行同时完成：
        #   1. 新价位：建一个空 OrderedDict 作为桶
        #   2. 已有价位：复用现有桶
        #   3. 把订单挂到桶里，id 作为 key（保留插入顺序 = 时间优先）
        # 相比"先 if key in book else ..."的分支写法，这里更 Pythonic。

        return order


    # 打印 bids & ask
    # example:
    # Bids | Asks #
    # Bid1 | Ask1 #
    def print_books_l2(self):
        # [AI 批注] ✅ 命名为 _l2 表明你理解了"内部存 L3、对外展示 L2"的区分，
        # 这是真实交易所的架构直觉，很棒。

        def format_rows(book: Book):
            return [
                (f"{price:.2f}", sum(o.quantity for o in bucket.values()), len(bucket))
                for price, bucket in book.items()
            ]
        # [AI 批注] ✅ 用内嵌 def 封装重复逻辑，比 lambda 更好（有名字、可多行、堆栈追踪友好）。
        # 三列一行的 tuple 结构正好对应 L2 行情的 (price, total_qty, order_count)。

        BEST_ASK = self.asks.peekitem(0)[0] if self.asks else None
        BEST_BID = self.bids.peekitem(0)[0] if self.bids else None
        spread = BEST_ASK - BEST_BID if BEST_ASK != None and BEST_BID != None else '-'
        # [AI 批注] ✅ 已修正。空盘口保护加上了，truthiness 判断 SortedDict 是否为空是正确做法。
        #
        # [AI 批注] ⚠️ 两个小问题：
        # 1. 命名：MAX_BID 没问题（best bid = 最高买价），但 MAX_ASK 有歧义——
        #    best ask 是最**低**卖价，叫 MIN_ASK 或 best_ask 更精确。
        # 2. 惯例：Python 里判断 None 推荐用 `is not None` 而非 `!= None`。
        #    因为 `!=` 可以被 __eq__ 重写，`is` 才是真正的身份比较。
        #    虽然对 float 无所谓，但养成习惯对后面写复杂类型有好处。
        
        bid_rows = format_rows(self.bids)
        ask_rows = format_rows(self.asks)
        rows = list(zip_longest(bid_rows, ask_rows , fillvalue=("", "", "")))
        # 把左右两组三列拼成一行六列
        flat = [(*bid_raw_row, *ask_raw_row, "") for bid_raw_row, ask_raw_row in rows]
        print(tabulate(flat, headers=["Bid Price", "Bid Qty", "Bid Cnt", "Ask Price", "Ask Qty", "Ask Cnt", f"Spread: {spread}"], tablefmt="grid"))
        # [AI 批注] ✅ 已修正。Bid 左 Ask 右 + Spread 只算第一档 + 空盘口保护，三个问题全部解决。


order_book = OrderBook()

# order_book.add_order(OrderRequest(
#     side=Side.BID,
#     price=100.00,
#     quantity=10
# ))
# order_book.add_order(OrderRequest(side=Side.ASK, price=101.0, quantity=8))
# order_book.add_order(OrderRequest(side=Side.BID, price=100.0, quantity=10))
# order_book.add_order(OrderRequest(side=Side.BID, price=99.5,  quantity=5))
# order_book.add_order(OrderRequest(side=Side.ASK, price=101.5, quantity=3))

order_book.print_books_l2()


# ============================================================
# [AI 批注] 📊 整体评价（第四轮）
# ============================================================
#
# 完成度：★★★★★ (5/5)  ↑ 从 4.5 提升
# - ✅ 所有代码 bug 已修复（_id_seq / timestamp / return / spread 语义 / 空盘口）
# - ✅ 思考题 Q2 和 Q3 都写了自己的理解
# - ✅ 主动测试了空盘口边界场景
#
# 代码质量：★★★★☆ (4.5/5)  持平
# - ✅ 空盘口保护用 truthiness 判断，简洁正确
# - ✅ spread 放 header 单次显示，语义和展示都对了
# - ⚠️ 小改进：MAX_ASK 命名不太精确（best ask 是最低价）；!= None 改 is not None 更 Pythonic
# - ⚠️ 记得把测试订单取消注释，验证有数据时输出也正常
#
# 理解深度：★★★★☆ (4/5)  持平
# - ✅ 思考题迈出了第一步，敢写自己的理解（哪怕不完美）很重要
# - ⚠️ Q2: "分歧越小"不是 spread 的本质。核心概念是 liquidity cost（立即成交的代价）
#         —— 详见上方批注
# - ⚠️ Q3: list 按下标访问是 O(1) 不是 O(n)；SortedDict key 查找是 O(log n) 不是 O(1)
#         —— 试着列 list vs SortedDict 的四操作复杂度对比表，写完理解会更扎实
#
# ------------------------------------------------------------
# 无需修正的必做项了。以下可选：
#
# 1. 🟢 修正 Q2/Q3 的表述精度（见上方批注）
# 2. 🟢 MAX_ASK → best_ask，!= None → is not None
# 3. 🟢 取消注释测试订单，确认有数据时输出正常
#
# ------------------------------------------------------------
# Task 1 已完成，可以进 Task 2。
#
# 🟢 进阶方向（进 Task 2 前可以想想）：
#
# - 试着挂一个"交叉价"订单（bid=102 而 ask 最低 101），
#   你会发现你的 add_order 允许这种订单进入订单簿，
#   但现实中这种订单应该立即触发撮合 —— 这就是 Task 2 的起点。
# ============================================================
