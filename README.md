### 自己随便鼓捣出来的脚本程序

##### 一、GetIP


* 统计nginx服务器上的access.log日志，输出结果如下：

> [23/Oct/2018:06:25:01] 至 [23/Oct/2018:20:24:21]  
> 单秒最大访问量:298  
> nginx访问ip个数:9095  
> nginx一共访问量:126555  
> 统计时间: 2018-10-24 13:57:09.287000  





* 统计nginx服务器上的error.log日志，输出结果如下:

> connect() to unix:///home/ubuntu/www/cmxsite/cmxsite.sock failed (111: Connection refused) while connecting to upstream,  
> directory index of "/home/ubuntu/www/html/home/" is forbidden,  
> rewrite or internal redirection cycle while processing "/index.php",  
> connect() to unix:///home/ubuntu/www/eleccard/eleccard.sock failed (111: Connection refused) while connecting to upstream,  
>
> 06:56:21 至 20:08:17  
> nginx error出现ip个数:87   
> nginx error类型个数:4   
> nginx error次数:98  
> 统计时间: 2018-10-24 17:16:36.199000  

2018-10-24  error的正则表达式 花费了我很多时间



##### 二、IMEIapp

* IMEIapp是一个django项目，作用是可以把excel（内容单纯为IMEI号）上传至项目中，再读取数据存入到mysql当中，进行后续处理

2018-10-23




##### 三、test_celery

* 是一个django项目，利用celery异步任务处理，上传文件后，不用等待逻辑执行完再return，逻辑在后台执行，不影响用户体验
* 挂在ubuntu服务器上 使用nginx uwsgi  supervisor 实现用户上传文件异步执行任务
* [我的博客](https://www.dogebug.cn)上有针对这个项目的详细文章

2018-12-27



**运行了很长时间的celery之后，发现有任务一直没有完成，也没有失败，一直处于执行当中，就去查看了celery的log**。

**截取了少部分error：**

```python
  File "/home/ubuntu/www/cmxcelery/kkwork/local/lib/python2.7/site-packages/MySQLdb/cursors.py", line 205, in execute
    self.errorhandler(self, exc, value)
  File "/home/ubuntu/www/cmxcelery/kkwork/local/lib/python2.7/site-packages/MySQLdb/connections.py", line 36, in defaulterrorhandler
    raise errorclass, errorvalue
OperationalError: (2006, 'MySQL server has gone away')
```

怀疑是执行任务时间过长（一个任务大概会花4、5个小时），mysql连接时间过长，但并没有操作mysql（只会在开始和结束的时候进行mysql操作），导致client和MySQL server之间的链接断开了。



最后的解决办法为 主动断开连接 再进行连接数据库操作

```python
from django.db import connection
from time import sleep


connection.close()
sleep(10)
```

2019-01-04