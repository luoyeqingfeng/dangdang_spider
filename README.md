## 1. 项目简介
1. 采用python语言，用scrpay框架爬取当当图书的一些信息
2. 数据库Mongdb
***
## 2. 基本环境
1. 操作系统：Windows10
2. 安装python3.7
3. 安装匹配工具
4. 安装scrapy框架
5. 安装mysql数据库
***
## 3. 安装scrapy出错的解决办法

##### 1. window安装出错
1. 下面门这个地址下载.whl文件
https://www.lfd.uci.edu/~gohlke/pythonlibs/
2. ctrl+f搜索Twisted，下载Twisted对应版本的whl文件，cp后面是python版本，amd64代表64位操作系统
3. 然后运行命令
```markdown
pip install 下载的 whl文件地址
```
4. 然后安装scrapy
```markdown
pip install scrapy
```
5. 安装分布式
```markdown
pip install scrapy_redis
```
***
## 4.scrapy五大核心组件工作流程
1. spider中的url被封装成请求对象交给引擎(每一个url对应一个请求对象)
2. 引擎拿到请求对象之后, 将其全部交给调度器
3. 调度器拿到所有请求对象后, 通过内部的过滤器过滤掉重复的url, 最后将去重后的所有url对应的请求对象压入到队列中, 随后调度器调度出其中一个请求对象, 并将其交给引擎
4. 引擎将调度器调度出的请求对象交给下载器
5. 下载器拿到该请求对象去互联网中下载数据
6. 数据下载成功后会被封装到response中, 随后response会被交给下载器
7. 下载器将response交给引擎
8. 引擎将response交给spiders
9. spiders拿到response后调用回调方法进行数据解析, 解析成功后产生item, 随后spiders将item交给引擎
10. 引擎将item交给管道, 管道拿到item后进行数据的持久化存储
***
## 4. 代码解释

##### 1.run.py文件
```markdown
#项目启动文件，Windows下运行命令：
python begen.py
```
##### 2.setting.py文件
1. 配置robots协议
```python
ROBOTSTXT_OBEY = False
```
2. 配置线程数
```python
CONCURRENT_REQUESTS = 32
```
3. 配置请求头（也可以不配置，在下载站中间件里面写）
```python
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
  "User-Agent":"Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50",
}
```
4. 配置下载器中间件
```python
DOWNLOADER_MIDDLEWARES = {
   'Dangdang.middlewares.DangdangDownloaderMiddleware': 543,
    'Dangdang.middlewares.RandomUaWares':400
}
```
5. 配置项目管道
```python
ITEM_PIPELINES = {
   'Dangdang.pipelines.DangdangPipeline': 299,
   'Dangdang.pipelines.MongoPipeline': 299,
   #分布式
   # 'example.pipelines.ExamplePipeline': 300,
   'scrapy_redis.pipelines.RedisPipeline': 400,
}
```
6. 配置Mongodb数据库
```python
MONGO_HONST="localhost"
DB_NAME="spider"
DB_SET="dangdang"
```
7. 配置分布式
```python
#分布式
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
SCHEDULER_PERSIST = True
```
##### 3. pipelines.py文件
项目管道：这个文件主要是把爬取的数据存入数据库
##### 4. middlewares.py文件
中间件文件：代理和user-agent都可以写在这个文件里面
##### 5. items.py文件
定义需要爬取数据的文件
##### 6. spiders下的dangdang.py文件
爬虫文件：自定义爬虫文件，把爬虫的逻辑代码都写在这个文件里面
