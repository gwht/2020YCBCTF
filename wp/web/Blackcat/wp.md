***\*Blackcat\****

***\*知识点：\****

1） PHP 基础代码审计

2）hash_hmac()函数绕过

 

***\*解题步骤：\****

1） 打开题目有“来听听歌休息一下吧”和一个MP3播放器，查看源代码，下载MP3。

![img](file:///C:\Users\60542\AppData\Local\Temp\ksohtml21032\wps1.jpg) 

 

2）用notepad打开mp3文件最后有一段源码，代码审计

 

![img](file:///C:\Users\60542\AppData\Local\Temp\ksohtml21032\wps2.jpg) 

3）hash_hmac()函数第二个参数为数组的时候，返回结果为NULL。则$clandestine可控，$hh就可以知道，下面判断即可绕过

 

```
White-cat-monitor[]=1&One-ear=;cat flag.php&Black-Cat-Sheriff=04b13fc0dff07413856e54695eb6a763878cd1934c503784fe6e24b7e8cdb1b6
```

