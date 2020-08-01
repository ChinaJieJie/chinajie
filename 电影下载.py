# -*- encoding: utf-8 -*-
"""
@File    : 电影下载.py
@Time    : 2020/6/30 3:57
@Author  : 杰哥哥
@Software: PyCharm
"""

import requests
'''
# http://jx.618g.com/?url=https://www.iqiyi.com/v_19rxtb5eo0.html#vfrm=19-9-0-1
# http://jx.618g.com/?url= 后面加上播放链接
# https://iqiyi.cdn27-okzy.com/20200626/5295_f282c658/1000k/hls/3cce9276bf1000000.ts
# 这是一小段视频的链接，这个视频共有1066段
# 下载完成后进行视频拼接  命令行中找到保存视频的文件夹 
cmd 
cd / 
D: 
cd move
copy /b *.ts +自定义视频名加后缀(copy /b *.ts name.mp4)
'''


def download(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0"
    }
    print(url)
    res = requests.get(url, headers=headers)
    # print(res.status_code)
    if res.status_code == 200:
        rest = res.content
        with open('D:/move/{}'.format(url[-10:]), 'wb') as f:
            f.write(rest)
    else:
        print('下载失败。。。')


def main():
    urls = 'https://iqiyi.cdn27-okzy.com/20200626/5295_f282c658/1000k/hls/3cce9276bf'

    for i in range(0, 1067):
        try:
            if i <= 9:
                url = urls + '100000%s.ts' % i
                download(url)
            elif i <= 99:
                url = urls + '10000%s.ts' % i
                download(url)
            elif i <= 999:
                url = urls + '1000%s.ts' % i
                download(url)
            elif i > 999:
                url = urls + '100%s.ts' % i
                download(url)
        except:
            pass


if __name__ == '__main__':
    main()