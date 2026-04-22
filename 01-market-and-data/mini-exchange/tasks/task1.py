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

from dataclasses import dataclass, field
from collections import OrderedDict
from enum import Enum
from sortedcontainers import SortedDict

Price = float
Quantity = int
OrderId = str

class Side(Enum):
    BID = "bid"
    ASK = "ask"

@dataclass
class Order:
    id: OrderId
    price: Price
    quantity: Quantity
    timestamp: str
    side: Side


@dataclass
class OrderBook:
    # 买单，高价优先，所以按照价格降序
    bids: SortedDict[Price, OrderedDict(OrderId, Order)] = SortedDict(lambda price: -price)

    # 卖单，低价优先，所以按照价格升序
    asks: SortedDict[Price, OrderedDict(OrderId, Order)] = SortedDict()

    # 接受限价单
    def add_order(_, order: Order):

        # 判断 order 类型，决定归档到哪里
        book = _.bids if order.side == Side.BID else _.asks

        book[order.price][order.id] = order

    # 打印 bids & ask
    def print_books(_):
        # TODO
        print()