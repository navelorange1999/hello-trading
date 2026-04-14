# 3.1 回测引擎 — 学习资源

## 回测原理

### 架构设计
- 搜索 "event driven backtesting system design"
  > 重点理解：为什么事件驱动比简单的循环更接近真实交易环境

- 搜索 "quantstart event driven backtesting"
  > QuantStart 的系列文章是经典参考，但注意是理解思路，不是照抄代码

### 回测陷阱
- 搜索 "backtesting pitfalls look ahead bias survivorship bias"
  > 这可能是整个学习路线中最重要的一篇阅读——不理解这些偏差，回测就是自我欺骗

- 搜索 "overfitting in trading strategy backtest"
  > 过拟合是回测的头号敌人，下一个项目中你会亲身体会

## 绩效指标

### 核心指标
- 搜索 "Sharpe ratio explained formula example"
  > 夏普比率是最通用的风险调整收益指标，但它有局限性

- 搜索 "Sortino ratio vs Sharpe ratio"
  > Sortino 只惩罚下行波动，更符合直觉

- 搜索 "maximum drawdown calculation"
  > 最大回撤是投资者最关心的指标之一——它回答了「最坏能亏多少」

### 进阶指标
- 搜索 "Calmar ratio information ratio"
  > 了解更多风险调整指标，但不需要全部实现

## Python 技术

### 面向对象设计
- 搜索 "python abstract base class ABC"
  > 策略接口的定义可以用 ABC，让不同策略有统一的接口

### 性能优化
- 搜索 "pandas vectorized operations vs iterrows"
  > 如果回测太慢，可能是因为你在逐行循环 DataFrame

## 已有框架（参考但不要直接使用）

- **Backtrader**: 搜索 "backtrader documentation"
  > 最流行的 Python 回测框架之一。在你写完自己的引擎后再看它，你会更深刻地理解它的设计选择

- **Zipline**: 搜索 "zipline backtesting"
  > Quantopian 开发的引擎，事件驱动架构的参考

- **vnpy**: 搜索 "vnpy 文档"
  > 中文社区最活跃的量化交易平台

> 重要：先自己写，再看框架。如果你先看框架，你会不自觉地照搬它的设计，失去独立思考的机会。
