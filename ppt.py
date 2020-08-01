# -*- encoding: utf-8 -*-
"""
@File    : ppt.py
@Time    : 2020/7/23 17:37
@Author  : 杰哥哥
@Software: PyCharm
"""
import json
import base64
import requests
from multiprocessing import Pool


def ppt(url):
    data = {
        'POST': '/opi/v1/search.ashx?fid=1111111111&size=48&keyword=P%20P%20T HTTP/1.1',
        'Host': 'ppt.sotary.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0',
        'Accept': 'text/plain, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Length': '1',
        'Origin': 'http://ppt.sotary.com',
        'Connection': 'keep-alive',
        'Referer': 'http://ppt.sotary.com/web/wxapp/index.html',
        'Cookie': 'Hm_lvt_d4d6f44a4134fe6961be077ddf3dd05a=1595501979,1595572849,1595572908,1595572953; '
                  'Hm_lpvt_d4d6f44a4134fe6961be077ddf3dd05a=1595572953',
        'Cache-Control': 'max-age=0',
    }
    try:
        response = requests.post(url, data=data).text
        js = base64.b64decode(response)
        test = json.loads(js)
        # print(test)
        for i in test['rows']:
            name = i['name']
            # print(name)
            fid = i['filepath']
            response_ppt = requests.get(fid).content
            with open('D:/download/PPT/{}.pptx'.format(name), 'wb') as f:
                print('正在下载：%s' % name)
                f.write(response_ppt)
    except:
        pass


def load():
    print('--------------------正在爬取第：第1页--------------------')
    ppt('http://ppt.sotary.com/opi/v1/search.ashx?fid=1111111111&size=48&keyword=')
    for i in range(1, 157):
        url = 'http://ppt.sotary.com/opi/v1/search.ashx?fid=%d&size=48&keyword=' % (i * 49)
        print('--------------------正在爬取第：%s页--------------------' % (i + 1))
        ppt(url)


if __name__ == '__main__':
    load()

