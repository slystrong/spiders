一.scrapy流程

![scrapy_1](images\scrapy_1.png)

Scrapy中的数据流由执行引擎控制,过程如下:

1、引擎打开⼀个⽹站(open a domain)，找到处理该⽹站的Spider并向该spider请求第⼀个要 爬取的URL(s)。 

2、引擎从Spider中获取到第⼀个要爬取的URL并在调度器(Scheduler)以Request调度。 

3、引擎向调度器请求下⼀个要爬取的URL。 

4、调度器返回下⼀个要爬取的URL给引擎，引擎将URL通过下载中间件(请求(request)⽅向)转 发给下载器(Downloader)。 

5、⼀旦⻚⾯下载完毕，下载器⽣成⼀个该⻚⾯的Response，并将其通过下载中间件(返回 (response)⽅向)发送给引擎。 

6、引擎从下载器中接收到Response并通过Spider中间件(输⼊⽅向)发送给Spider处理。 

7、Spider处理Response并返回爬取到的Item及(跟进的)新的Request给引擎。 

8、引擎将(Spider返回的)爬取到的Item给Item Pipeline，将(Spider返回的)Request给调度 器。 

9、(从第⼆步)重复直到调度器中没有更多地request，引擎关闭该⽹站。 