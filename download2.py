#!/usr/bin/env python
import os
from pyquery import PyQuery as pq

class ButianDownloader():
    def __init__(self):
        os.chdir('html')
        self.url = "https://loudong.360.cn/Loo/index/p/{0}.html"
        self.f = "{0}.html"

    def init_pq(self, url, element):
        self.doc = pq(url)
        return self.doc(element)

    def download(self, element):
        try:
            for i in xrange(1, 4614):
                u = self.url.format(i)
                f = self.f.format(i)
                ele = self.init_pq(u, element)
                print "[*] " + u + "-> " + f
                with open(f, 'w') as file:
                    file.write(ele.text().encode('utf-8'))
        except KeyboardInterrupt:
            pass

if __name__ == '__main__':
    ButianDownloader().download('dd')
