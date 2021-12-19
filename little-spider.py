import urllib.request
from io import BytesIO
import gzip
import re
import time
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
url = 'http://www.biquge.info/26_26516/'
req = urllib.request.Request(url=url, headers=headers)
res = urllib.request.urlopen(req)
buff = BytesIO(res.read())
f = gzip.GzipFile(fileobj=buff)
html = f.read().decode()
a = re.compile('<dd><a href="(.*?)" .*?>(.*?)</a></dd>', re.S)
b = a.findall(html)
print(b)
print(b[1:2])
for i in b:
    time.sleep(1)
    print(i)
    detail_url = url+i[0]
    print(detail_url)
    flag = True
    while flag:
        # 获取详情地址所对应的源码信息
        try:
            req = urllib.request.Request(url=url, headers=headers)
            res = urllib.request.urlopen(detail_url)
            h = res.read()
            try:
                buff = BytesIO(h)
                f = gzip.GzipFile(fileobj=buff)
                html = f.read().decode()
            except:
                html = h.decode()
            print(html)
        except:
            flag = True
        d = re.compile('<div id="content"><!--go-->(.*?)</div>', re.S)
        data = d.findall(html)
        print(data)
        # 将小说写入文件中
        with open('凡人聊天群.txt', 'a+', encoding='utf-8') as f:
            f.write(i[1])
            f.write('\n')
            ff = data[0].replace('&nbsp;', ' ').replace(
                '<br/>', '\n').replace('<!--over-->', ' ')
            f.write(ff)
            f.write('\n')
        flag = False
