# -*- encoding: utf-8 -*-
"""
@File    : BaiduMusic.py
@Time    : 2020/7/27 20:56
@Author  : 杰哥哥
@Software: PyCharm
"""
import requests
from lxml import etree
import json
from multiprocessing import Pool


def Baidi_Music(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0"
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            html = etree.HTML(response.text)
            res = html.xpath('//div[@class="top-list-item"]/div[1]/div/ul')
            for i in res:
                music_id = i.xpath('./li/div/span[4]/a/@href')
                for li in range(3):
                    del music_id[0]
                for j in music_id:
                    response_url = requests.get(urls + j, headers=headers)
                    if response_url.status_code == 200:
                        mp3_url = 'http://musicapi.taihe.com/v1/restserver/ting?method=baidu.ting.song.playAAC&format' \
                                  '=jsonp' \
                                  '&songid=%s&from=web ' % j[6:15]
                        response_mp3 = requests.get(mp3_url, headers=headers)
                        if response_mp3.status_code == 200:
                            try:
                                name = json.loads(response_mp3.text)['songinfo']
                                music_name = name['title']
                                js = json.loads(response_mp3.text)['bitrate']
                                format = js['file_extension']
                                download = requests.get(js['show_link'], headers=headers).content
                                with open('D:/download/music/{}.{}'.format(music_name, format), 'wb') as f:
                                    print('正在下载：{}'.format(music_name))
                                    f.write(download)
                            except KeyError:
                                pass
                        else:
                            print('网页请求失败！')
                    else:
                        print('网页请求失败！')
        else:
            print('网页请求失败！')
    except:
        pass


if __name__ == '__main__':
    url = 'http://music.taihe.com/top/new'
    urls = 'http://music.taihe.com'
    Baidi_Music(url)
    pool = Pool(5)
    pool.apply_async(Baidi_Music, args=(url,))
    pool.close()
    pool.join()
