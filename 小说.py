# -*- encoding: utf-8 -*-
"""
@File    : 小说.py
@Time    : 2020/7/5 23:49
@Author  : 杰哥哥
@Software: PyCharm
"""

import requests
from lxml import etree


def biquge(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0"
    }

    # 请求网页
    res = requests.get(url, headers=headers)
    # 更换网页格式
    res.encoding = 'gbk'
    # 解析网页
    response = etree.HTML(res.text)
    # 如果网页请求成功执行下面代码
    if res.status_code == 200:
        # 获取小说标题
        biaoti = response.xpath('//div[@class="content"]/h1/text()')
        # 获取小说内容节点
        html = response.xpath('//div[@id="content"]')
        try:
            # 获取下一章小说网页
            for i in html:
                # 获取小说内容页面
                for j in range(len(i)):
                    # 提取小说内容文字到字典
                    list_1 = {'txt': i.xpath('./text()')[j]}
                    # 将字典内容转换为字符串
                    data = str(list_1['txt'])
                    # 打印每一章小说内容
                    print(data)
                    # 将小说标题命名并保存小说内容
                    with open('D:/move/{}.txt'.format(biaoti[0]), 'a', encoding='utf-8') as f:
                        f.write(data)
                        f.write('\n')
        except:
            pass
        download(response, biaoti)
    else:
        # 如果网页请求失败执行
        print('网页请求失败！')
        # 将获取到的网页信息传给download函数


def download(response, biaoti):
    # 将传递过来的网页提取下一页的链接
    try:
        t = response.xpath('//div[@class="page_chapter"]//li[3]/a/@href')
        # 将提取出来的链接加上头网页
        g = 'http://www.biqiuge.com' + t[0]
        # 再次调用上面函数进行循环
        biquge(g)
    except IndexError:
        print('爬取完毕！')
    except:
        print('爬取出现异常！，爬取到{}'.format(biaoti[0]))


if __name__ == '__main__':
    # 小说第一章内容网址
    url = 'https://www.biqiuge.com/book/60076/573572216.html'
    biquge(url)
