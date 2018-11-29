# coding:utf-8
# python小爬虫：贴吧图片的爬取
import re
import urllib.request


def get_html(url):
    page = urllib.request.urlopen(url)
    html = page.read().decode("utf-8")
    return html


def get_image(html_code):
    reg = r'src="(.+?\.jpg)" width'
    reg_img = re.compile(reg)  # 编译一下，运行更快
    img_list = reg_img.findall(html_code)
    x = 0
    for img in img_list:
        urllib.request.urlretrieve(img, '%s.jpg' % x)
        x += 1
        print(img)


print("-------网页图片抓取-----")
print(u'请输入url:'),
url = input()
if url:
    pass
else:
    print("------没有地址输入正在使用默认地址--------")
    url = 'http://tieba.baidu.com/p/1753935195'
print("-------正在获取网页------")
html_code = get_html(url)
print("-------正在下载图片------")
get_image(html_code)
print("-------下载图片成功------")
input("Press Enter to exit")
