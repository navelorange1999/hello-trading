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
#
# Q3: 为什么不能用简单 list？什么结构更合适？
#     你实际上已经用 SortedDict 回答了，但没把"为什么"写下来。
#     提示：列表在中间插入是 O(n)，按价格查最优档是 O(n)；真实交易所每秒几十万笔，
#     必须 O(log n) 级别。SortedDict 背后是 B-tree 变种，正好符合需求。
#     关键词：time complexity、red-black tree、skip list

from dataclasses import dataclass, field
from collections import OrderedDict
from enum import Enum
from sortedcontainers import SortedDict

# 在 terminal 打印表格
from tabulate import tabulate

# 自增 ID（有序、便于排查、还能作 tie-breaker）：
from itertools import count

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
    timestamp: str
    # [AI 批注] ❌ 类型标注错了。你在 add_order 里写的是 time.time_ns()，
    # 这个函数返回 int（纳秒整数，类似 1729123456789012345），不是 str。
    # 类型应该是 int。
    #
    # 为什么这事重要：撮合引擎里时间戳要参与"时间优先"比较，用 int 直接比较 O(1)，
    # 而 str 比较是字典序——"10" < "9" 会出大问题。


Book = SortedDict[Price, OrderedDict[OrderId, Order]]
# [AI 批注] ✅ 这个类型别名提炼得特别好。
# 一眼就能看出数据结构的三层语义：
# - 外层 SortedDict：按价格排序（价格优先）
# - 内层 OrderedDict：按插入顺序存储同价位订单（时间优先）
# - value 是 Order：完整订单信息
# 这个别名后面在 print_books_l2 的 format_rows 参数里复用了，语义清晰度+1。


@dataclass
class OrderBook:
    _id_seq = count(1)
    # [AI 批注] ❌ 自己打脸了！你下面 bids/asks 都正确用了 field(default_factory=...)
    # 来避开"可变默认值陷阱"，但 _id_seq 又踩回去了。
    #
    # count(1) 在 class 定义时求值一次，所有 OrderBook 实例共享同一个迭代器。
    # 验证：
    #   a = OrderBook(); b = OrderBook()
    #   a.add_order(...); b.add_order(...)  # b 的 order.id 会接着 a 的继续涨
    #
    # 修复方式和 bids/asks 一样：
    #   from typing import Iterator
    #   _id_seq: Iterator[int] = field(default_factory=lambda: count(1))
    #
    # 顺便想一下：真实交易所里一个 OrderBook 对应一个交易对（BTC/USDT、AAPL），
    # 不同交易对的 order id 应不应该共享？这个 bug 在单交易对时看不出来，
    # 上多交易对就会炸。

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
        # [AI 批注] ⚠️ 签名声明返回 Order，但下面没有 return。
        # 调用方现在拿到的其实是 None，类型检查器会报警告。
        # 要么删掉 -> Order 标注，要么在函数末尾加 return order。
        # 真实撮合引擎里调用方一定需要拿到新建订单的 id（用来后续 cancel / modify），
        # 所以应该 return。

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

        bid_rows = format_rows(self.bids)
        ask_rows = format_rows(self.asks)
        rows = list(zip_longest(ask_rows, bid_rows , fillvalue=("", "", "")))
        # 把左右两组三列拼成一行六列
        flat = [(*a, *b) for a, b in rows]
        print(tabulate(flat, headers=["Ask Price", "Ask Qty", "Ask Cnt", "Bid Price", "Bid Qty", "Bid Cnt"], tablefmt="grid"))
        # [AI 批注] ⚠️ 左右顺序和市场惯例相反。
        # 几乎所有交易所界面（Binance、Nasdaq、东方财富）都是 "Bid 左 | Ask 右"，
        # 或上下布局时 "Ask 上（由高到低）| Bid 下（由高到低）"，spread 在中间。
        # 你现在是 "Ask 左 | Bid 右"，看的人会下意识反应不过来。
        # 试着 swap 一下，再看看哪种更符合你在交易软件里见到的样子。
        #
        # 另外思考：spread 本身没有单独显示。第一行其实就是 best ask 和 best bid，
        # 可以在表格上方加一行 "Spread: X.XX"，这是行情截图里最显眼的信息之一。




order_book = OrderBook()

order_book.add_order(OrderRequest(
    side=Side.BID,
    price=100.00,
    quantity=10
))
order_book.add_order(OrderRequest(side=Side.ASK, price=101.0, quantity=8))
order_book.add_order(OrderRequest(side=Side.BID, price=100.0, quantity=10))
order_book.add_order(OrderRequest(side=Side.BID, price=99.5,  quantity=5))
order_book.add_order(OrderRequest(side=Side.ASK, price=101.5, quantity=3))

order_book.print_books_l2()


# ============================================================
# [AI 批注] 📊 整体评价
# ============================================================
#
# 完成度：★★★★☆ (4/5)
# - ✅ OrderBook 类、限价单接收、买卖分档、排序都实现了
# - ✅ 额外做了 L2 视图（聚合量能和订单数），超出题目要求
# - ⚠️ 思考题只答了 1/3（只答了排序规则，没答 spread 含义和"为什么不用列表"）
# - ⚠️ 测试数据较薄，缺少"交叉价" / "多档深度" 等边界场景
#
# 代码质量：★★★★☆ (4/5)
# - ✅ OrderRequest/Order 分层、Book 类型别名、setdefault 一行挂单、内嵌 format_rows
#      都是很成熟的 Pythonic 写法
# - ✅ 注释质量高，解释了"为什么"而不是"做什么"（比如 default_factory 的解释）
# - ❌ _id_seq 是类属性，踩了可变默认值的陷阱（和 bids/asks 原本的 bug 同源）
# - ❌ timestamp 类型标注为 str，实际是 int
# - ⚠️ add_order 声明 -> Order 但没 return
#
# 理解深度：★★★★☆ (4/5)
# - ✅ "价格优先 + 时间优先" 的规则翻译成数据结构（SortedDict 套 OrderedDict）
#      证明你抓住了订单簿的本质
# - ✅ 区分 L2/L3 行情展示说明你对"交易所对外数据契约"有初步直觉
# - ⚠️ 对 spread 的经济含义还没形成自己的解读，这是理解市场的关键一步
# - ⚠️ 对"为什么选 SortedDict 而非 heapq/list"背后的复杂度权衡还没显式讨论
#
# ------------------------------------------------------------
# 需要修正的 4 件事（按优先级）：
#
# 1. 🔴 _id_seq 改用 field(default_factory=lambda: count(1))
#       —— 多实例共享 id 是真的 bug，不是洁癖
#
# 2. 🔴 Order.timestamp 类型标注从 str 改成 int
#       —— 当前标注和实际值不符，会误导 reader 和类型检查器
#
# 3. 🟡 add_order 末尾加 return order（或删掉 -> Order 标注）
#       —— 下一个 task 做撮合时，调用方要拿到订单对象检查状态
#
# 4. 🟡 回到文件顶部补齐思考题 Q2 和 Q3 的思考
#       —— 这比修 bug 更重要。你现在的代码是对的，但没把"为什么这样设计"沉淀下来
#
# ------------------------------------------------------------
# 🟢 进阶方向（做完再想）：
#
# - 表格加一行 "Spread: X.XX"，这是 L2 行情最核心的一个衍生指标
# - 左右顺序改成 "Bid 左 | Ask 右"，对齐主流交易所 UI
# - 试着挂一个"交叉价"订单（bid=102 而 ask 最低 101），
#   你会发现你的 add_order 允许这种订单进入订单簿，
#   但现实中这种订单应该立即触发撮合 —— 这就是 Task 2 的起点。
# ============================================================
