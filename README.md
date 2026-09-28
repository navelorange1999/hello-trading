# Hello Trading

> 用工程方法训练投资思维，而不是寻找“必胜策略”。

这个仓库的目标不是做一个自动赚钱机器人，也不是收集越来越多的指标，而是建立一套可以长期迭代的 **Investment / Trading Operating System**：

**知识 → 假设 → 数据 → 研究 → 估值 → 决策 → 风控 → 复盘 → 修正**

## 为什么重构这个仓库

最初的内容更偏工程化交易系统：市场数据、技术指标、回测、风控、paper trading。

这些能力仍然保留，但新的主目标是：

1. 系统学习投资，而不是只学交易工具；
2. 提高对公司、行业、宏观和市场预期的理解；
3. 训练“事实 / 预期 / 价格”之间的关系；
4. 把每一次判断变成可复盘、可纠错的过程；
5. 利用 Python / AI / 数据能力降低研究成本，但不把判断外包给工具。

---

## 三条学习线

### A. Investment Foundation — 主线

以 **CFA Level I** 为主要知识框架，建立完整投资地图：

- Financial Statement Analysis
- Equity
- Corporate Finance
- Economics
- Fixed Income
- Quantitative Methods
- Portfolio Construction
- Derivatives
- Alternative Investments
- Ethics

CPA 不作为第二条应试主线，而作为 **财务深挖工具**，重点补：

- 收入确认
- 存货
- 固定资产 / 无形资产
- 资产减值
- 所得税
- 企业合并
- 商誉
- 长期股权投资
- 合并报表

入口：[00-roadmap](00-roadmap/)

### B. Research & Thinking — 核心实践线

每学一个知识点，都要尝试落到真实市场：

- 公司研究
- 行业研究
- 估值
- 预期差
- 事件驱动分析
- 市场日志
- Investment Note
- Decision Journal

入口：

- [06-company-research](06-company-research/)
- [07-market-thinking](07-market-thinking/)
- [08-review-system](08-review-system/)

### C. Engineering Lab — 工程实验线

原有 Chapter 1–5 全部保留，用来验证假设和建立研究基础设施：

- [01-market-and-data](01-market-and-data/) — 市场机制与数据
- [02-analysis-methods](02-analysis-methods/) — 技术 / 基本面分析
- [03-strategy-and-backtesting](03-strategy-and-backtesting/) — 策略与回测
- [04-risk-and-portfolio](04-risk-and-portfolio/) — 风险与组合
- [05-trading-system](05-trading-system/) — 执行、日志与反馈

工程能力服务于投资判断，而不是反过来。

---

## 推荐学习比例

长期阶段：

- **70% CFA**
- **15% CPA《会计》**
- **15% 公司 / 市场实践**

正式进入 CFA 考前冲刺后：

- **90% CFA**
- **10% 复盘 / 轻量实践**
- CPA 暂停或极低频

---

## 每周节奏

建议每周投入约 8 小时：

| 时间 | 内容 |
|---|---|
| 3 × 1h | CFA 新知识 |
| 1 × 1h | CFA 题目 / 错题 |
| 1 × 1h | CPA 深挖一个财务主题 |
| 1 × 2h | 公司 / 行业研究 |
| 1 × 1h | 周度复盘、预期差训练 |

学习的最小闭环不是“看完一章”，而是：

> 学到一个概念 → 做题 → 用真实案例解释 → 写下判断 → 一段时间后复盘

---

## CFA 报名 Gate

前期可以先学习，不急于报名。只有当下面条件大部分满足，再把报名费变成“考试门票”，而不是“逼自己学习的押金”。

- [ ] Level I syllabus 第一轮完成
- [ ] 各 Topic 题目大部分能稳定到一个可靠水平
- [ ] 英文题干阅读不再明显拖慢做题
- [ ] 至少做过 2 次完整模拟
- [ ] 能在规定节奏内完成模拟
- [ ] 已完成至少 4 份 Investment Note
- [ ] 有持续维护的 Error Log
- [ ] 自己能说清楚最薄弱的 3 个 Topic

> 注：这里的分数线是个人训练 Gate，不代表 CFA Institute 官方通过线。

---

## 研究时最重要的五个问题

研究任何股票之前，先回答：

1. **What is true?** — 事实是什么？
2. **What does the market expect?** — 市场已经预期了什么？
3. **What is different from expectation?** — 预期差在哪里？
4. **What is priced in?** — 当前价格已经反映了多少？
5. **What would prove me wrong?** — 什么证据会推翻我的判断？

如果这五个问题答不出来，先不要讨论“买不买”。

---

## 每月最低产出

每个月至少完成：

- 1 份 [Investment Note](06-company-research/templates/investment-note.md)
- 4 次 [Expectation Gap 训练](07-market-thinking/templates/expectation-gap.md)
- 1 次 [Monthly Review](08-review-system/templates/monthly-review.md)
- 持续维护 [Error Log](08-review-system/templates/error-log.md)

一年后，比“看了多少书”更重要的是：

- 你研究过哪些公司；
- 哪些判断后来被证伪；
- 你最常犯什么错误；
- 你在哪些行业逐渐形成了可迁移的认知。

---

## 原则

- **Outcome ≠ Decision Quality**：赚钱的交易可能是坏决策，亏钱的交易也可能是好决策。
- **Price is not value**：好公司不等于好投资。
- **Narrative needs numbers**：故事必须能落到收入、利润、现金流和资本回报。
- **Valuation is assumptions**：估值不是精确答案，而是一组可检验假设。
- **Risk first**：先考虑错误时会发生什么，再考虑正确时能赚多少。
- **AI is a research multiplier, not a decision maker**：AI 用来压缩信息处理成本，不替你承担判断责任。

---

## Start Here

第一次打开仓库时：

1. 阅读 [00-roadmap](00-roadmap/)
2. 创建第一份公司研究：[Investment Note Template](06-company-research/templates/investment-note.md)
3. 开始维护 [Error Log](08-review-system/templates/error-log.md)
4. 每周完成一次 [Expectation Gap](07-market-thinking/templates/expectation-gap.md)
5. 再根据需要进入原有 Chapter 1–5 做工程实验

