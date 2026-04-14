# 1.2 市场数据管道 — 学习资源

## 数据获取

### 股票数据
- **yfinance**  
  搜索 "yfinance documentation" — 免费获取美股、港股、部分 A 股数据
  > 最简单的入门方式，几行代码即可获取历史数据

- **AkShare**  
  搜索 "akshare 文档" — 国内开源金融数据库，覆盖 A 股、基金、期货
  > A 股数据的首选免费方案

- **Tushare**  
  搜索 "tushare pro" — 需要注册获取 token，数据更全面
  > 社区活跃，文档是中文的

### 加密货币数据
- **ccxt**  
  搜索 "ccxt python documentation" — 统一 API 覆盖 100+ 交易所
  > 重点看 `fetch_ohlcv` 方法，这是你最常用的

- 各交易所自己的 API 文档（Binance, OKX 等）
  > ccxt 够用了就不需要直接用，但了解底层有助于调试问题

## 数据处理

### pandas 核心操作
- **pandas 官方 10 分钟入门**  
  搜索 "pandas 10 minutes to pandas"
  > 如果 pandas 不熟，从这里开始。重点掌握 DataFrame、索引、切片、聚合

- **pandas 时间序列功能**  
  搜索 "pandas time series documentation"
  > 金融数据本质是时间序列，pandas 对此有很好的支持。关注 `DatetimeIndex`, `resample`, `rolling`

### 数据清洗
- 搜索 "handling missing data in financial time series"
  > 金融数据的缺失值处理和普通数据不同——停牌和真正的数据丢失要区别对待

### 复权处理
- 搜索 "stock split adjusted price explanation"
  > 理解为什么不做复权处理会让你的分析完全错误

## 可视化

### matplotlib 基础
- **matplotlib 官方教程**  
  搜索 "matplotlib tutorials"
  > 你需要掌握的核心：figure/axes 概念、plot、bar、patches.Rectangle

### K 线图原理
- 搜索 "candlestick chart explained"
  > 先理解概念，再动手画。每根蜡烛编码了 4 个价格信息。

## 统计基础

- 搜索 "quantitative finance basic statistics returns volatility"
  > 不需要统计学教科书，只需要理解收益率、波动率、相关性这三个核心概念

- 搜索 "log returns vs arithmetic returns finance"
  > 这是一个看似简单但影响深远的选择

## 存储方案比较

- **CSV**: 最简单，人类可读，但大数据量时慢
- **SQLite**: 搜索 "python sqlite3 tutorial" — 结构化查询，无需额外服务器
- **Parquet**: 搜索 "pandas parquet tutorial" — 列式存储，读写快，省空间
  > 建议从 CSV 开始，数据量大了再迁移到 Parquet
