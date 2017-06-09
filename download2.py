#!/usr/bin/env python
import os
from pyquery import PyQuery as pq

class ButianDownloader():
    def __init__(self):
        DIR_PATH = 'html'
        if not os.path.isdir(DIR_PATH):
            print '[!] dir not exists'
            print '[*] making dir...'
            os.mkdir(DIR_PATH)
        os.chdir(DIR_PATH)
        self.url = "https://loudong.360.cn/Loo/index/p/{0}.html"
        self.f = "{0}.html"

    def init_pq(self, url, element):
        self.doc = pq(url)
        return self.doc(element)

    def download(self, element):
        try:
            for i in xrange(1, 4619):
                u = self.url.format(i)
                f = self.f.format(i)
                ele = self.init_pq(u, element)
                print "[*] " + u + " -> " + f
                with open(f, 'w') as file:
                    count = 30
                    for j in ele.items(element):
                        file.write(j.text().encode('utf-8') + '\n')
                        count=count-1
                        if count == 0:
                            break
        except KeyboardInterrupt:
            pass

if __name__ == '__main__':
    ButianDownloader().download('dd')
