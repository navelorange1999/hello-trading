# 5.1 模拟交易系统 — 学习资源

## 系统设计

- 搜索 "algorithmic trading system architecture overview"
  > 了解成熟交易系统的模块组成，但不要过度设计——你的第一版应该是最简单可用的

- 搜索 "microservices vs monolith for trading system"
  > 对于个人项目，单体应用足够了。了解微服务是为了知道以后可以怎么扩展。

## 定时任务与自动化

- 搜索 "python schedule library tutorial"
  > 最简单的方式——在 Python 内部做定时调度

- 搜索 "crontab tutorial linux"
  > 更可靠的方式——用操作系统的 cron 来触发你的脚本

- 搜索 "python APScheduler tutorial"
  > 比 schedule 更强大的调度库，支持错过任务的处理

## 告警与通知

- 搜索 "python send email smtplib tutorial"
  > 最基础的告警方式，不需要依赖第三方服务

- 搜索 "telegram bot python aiogram" 或 "python-telegram-bot"
  > Telegram Bot 是个人项目告警的绝佳选择：免费、实时、支持富文本

- 搜索 "server酱 pushplus 微信推送"
  > 如果你更习惯用微信接收通知

## 模拟交易平台（参考）

- 搜索 "paper trading platform free"
  > 一些券商提供模拟交易功能（如 Interactive Brokers、富途），可以和你的系统做交叉验证

## 部署（可选进阶）

- 搜索 "python script run on cloud server"
  > 如果你希望系统 24/7 运行，考虑部署到云服务器

- 搜索 "docker python application tutorial"
  > Docker 可以让你的系统在任何机器上一致运行

## 从模拟到实盘（了解即可）

- 搜索 "Interactive Brokers API Python"
  > IB 是个人量化交易者最常用的经纪商之一

- 搜索 "ccxt exchange trading API"
  > ccxt 不只能获取数据，也支持下单——但先在测试网（testnet）上试

- 搜索 "Binance testnet paper trading"
  > 币安提供测试网，可以用虚拟资金做真实的 API 交易练习
