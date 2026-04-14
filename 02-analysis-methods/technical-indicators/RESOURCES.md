# 2.1 技术指标实验室 — 学习资源

## 指标原理

### 移动平均线
- 搜索 "simple moving average vs exponential moving average"
  > 先理解概念差异，再关注计算细节

- 搜索 "EMA smoothing factor derivation"
  > 理解 α = 2/(N+1) 的来源会帮你理解 EMA 的本质

### RSI
- 搜索 "RSI relative strength index Wilder original"
  > 注意区分 Wilder 的平滑方法和普通 EMA 的区别——这是很多人容易混淆的点

### MACD
- 搜索 "MACD indicator Gerald Appel"
  > MACD 的发明者 Gerald Appel 的原始意图是什么？和现在人们的用法一样吗？

### 布林带
- 搜索 "Bollinger Bands John Bollinger"
  > John Bollinger 自己写过一本书，他对自己发明的指标有哪些使用建议？

## 统计验证

### 假设检验基础
- 搜索 "hypothesis testing for beginners"
  > 你不需要成为统计学家，但需要理解「统计显著性」意味着什么

- 搜索 "p-value explained simply"
  > 重点理解：p 值不是「策略有效的概率」

### 金融中的统计陷阱
- 搜索 "multiple testing problem trading strategies"
  > 如果你测试了 100 个策略，总会有几个「看起来有效」——这就是多重检验问题

- 搜索 "fat tails kurtosis financial returns"
  > 股票收益率不服从正态分布，这对所有基于正态假设的指标（如布林带）意味着什么？

## Python 实现参考

### numpy 核心操作
- 搜索 "numpy cumulative operations cumsum cumprod"
  > 累计收益率的计算会用到

### 可视化进阶
- 搜索 "matplotlib subplot tutorial"
  > 多个指标需要多个子图，掌握 subplot 的布局方式
- 搜索 "matplotlib twinx secondary axis"
  > 价格和成交量共享 x 轴但需要不同的 y 轴刻度

## 延伸（可选）

- 搜索 "technical analysis academic research evidence"
  > 学术界对技术分析的看法比你想象的复杂——既不是完全无用，也不是致富密码

- **《Evidence-Based Technical Analysis》 by David Aronson**
  > 如果你对「技术分析到底有没有科学依据」这个问题感兴趣，这本书用严格的统计方法回答了它
