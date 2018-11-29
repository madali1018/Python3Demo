# coding:utf-8
# python小爬虫：获取网页源代码
# 参考：爬虫  http://www.cnblogs.com/Axi8/p/5757270.html

import urllib.request

page = urllib.request.urlopen('http://tieba.baidu.com/p/1753935195')  # 打开网页
htmlcode = page.read()  # 读取页面源码
print(htmlcode)  # 控制台输出
