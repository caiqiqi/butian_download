#coding=utf-8
#!/usr/bin/env python
import Queue
import requests
import re

url = ''
headers = {
    'Host': 'loudong.360.cn',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:53.0) Gecko/20100101 Firefox/53.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Cookie': '__guid=137882464.1989274523815992000.1457120065464.0173; __huid=10OeYK8UWNk%2BmVUf7EUN6kO09V1yBKvJdEuXGjkugVnFc%3D; __gid=67796994.778793401.1491330338020.1491338015642.17; UM_distinctid=15b3a370d1b4d3-033e82d5e623a28-49536b-fa000-15b3a370d1cc8; PHPSESSID=rsgqqhig92vuuiecsgscb5reb3; __q__=1496942773476; test_cookie_enable=null; _currentUrl_=%2FLoo%2Findex%2Fp%2F1.html; quCryptCode=2V3Qdc%252BWb6%252BTkB0SrDzTR0VQDFvmxyFrObB4dsQGzupLJ312K0263sxpPjNWr30WOOK%252FE5MzyJg%253D; quCapStyle=1; Q=u%3D360H395526072%26n%3D%26le%3D%26m%3DZGZ2WGWOWGWOWGWOWGWOWGWOZQL1%26qid%3D395526072%26im%3D1_t00df551a583a87f4e9%26src%3Dpcw_webscan%26t%3D1; T=s%3D543a5559f88446f437f20f4cac018dde%26t%3D1496926098%26lm%3D%26lf%3D2%26sk%3D7c3001f29d11e3a3d6744709a181add0%26mt%3D1496926098%26rc%3D%26v%3D2.0%26a%3D0',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Cache-Control': 'max-age=0',
}

s = requests.Session()

q = Queue.Queue()
for i in xrange(1, 4614):
    url = 'https://loudong.360.cn/Loo/index/p/{0}.html'.format(i)
    q.put(url)
try:
    while not q.empty():
        u = q.get()
        print u
        r = s.get(u, headers=headers)
        matched = re.findall(r"<dd><span>(.*?)</span><span>(.*?)</span>(.*?)<dd>", r.content)
        if matched:
            for i in matched:
                print i
except KeyboardInterrupt:
    pass
