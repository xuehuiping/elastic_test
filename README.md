为了对比效果，我们再部署一份ElasticSearch，看看向量搜索和传统文本搜索在效果层面的区别。

使用的数据相同。


```
scp elasticsearch-7.3.1-linux-x86_64.tar.gz  root@172.17.22.6:~/

tar -zxvf elasticsearch-7.3.1-linux-x86_64.tar.gz 
```

```
conf/目录是配置文件，可以适当替换
```


查询串：学习好辛苦哦

结果：
```
11.181026 决定这周起好好学习
10.14626 大家都好好哦
8.797304 辛苦工作回来，想和陌生人聊天的冲动忍住了，求表扬
8.231066 这学期开学到现在真的好努力呢，每天都能坚持用高效率学习，觉得自己好棒啊
7.987249 永远没有学习方法
7.7054224 不断学习画画，求表扬！
7.7054224 在家学习两天，快吐了！
7.4428086 雅思继续学习中求表扬
6.9678526 中午午休我还在学习 求夸夸
6.549879 决定学习到今天晚上九点，求表扬
```