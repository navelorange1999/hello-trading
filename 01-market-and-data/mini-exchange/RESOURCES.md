# 1.1 迷你交易所 — 学习资源

## 核心概念

### 市场微观结构
- **Investopedia: Order Book**  
  搜索 "investopedia order book" — 理解订单簿的基本组成
  > 重点关注：bid, ask, spread, depth 这几个概念

- **Investopedia: Market vs Limit Orders**  
  搜索 "investopedia market order vs limit order"
  > 重点关注：两种订单类型的执行方式有什么本质区别

### 撮合机制
- **搜索关键词**: "exchange matching engine algorithm price time priority"
  > 重点理解：为什么是「价格优先」而不是「时间优先」排第一？

### 价格形成
- **搜索关键词**: "how prices are formed in financial markets"
  > 思考：价格是一个「事实」还是一个「共识」？

## Python 技术

### 数据结构选择
- **Python 官方文档: heapq 模块**  
  搜索 "python heapq documentation"
  > 最小堆天然适合卖方排序，买方需要想想怎么处理

- **sortedcontainers 库**  
  搜索 "python sortedcontainers sortedlist"
  > 比 heapq 更灵活，支持快速插入和有序遍历。对比两者的优劣。

### 可视化
- **matplotlib 官方教程**  
  搜索 "matplotlib pyplot tutorial"
  > 本项目只需要基础的折线图和柱状图，不需要学高级用法

## 延伸阅读（可选）

- **《Flash Boys》 by Michael Lewis**  
  > 关于高频交易的通俗读物，能帮你理解为什么市场微观结构对某些人来说价值数十亿

- **搜索 "agent-based model financial market"**  
  > 用模拟交易者来研究市场行为是一个真实的学术研究方向

## 加密货币补充

- 去任何一个加密货币交易所（如 Binance）的交易界面，观察实时的订单簿变化
  > 加密货币市场 24/7 运行，是观察订单簿动态的绝佳窗口
