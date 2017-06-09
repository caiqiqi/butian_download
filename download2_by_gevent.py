#coding=utf-8
#!/usr/bin/env python
import os
from gevent.queue import Queue
import gevent
from pyquery import PyQuery as pq

class ButianDownloader():
    def __init__(self):
        DIR_PATH = 'html2'
        if not os.path.isdir(DIR_PATH):
            print '[!] dir not exists'
            print '[*] making dir...'
            os.mkdir(DIR_PATH)
        os.chdir(DIR_PATH)
        self.u = "https://loudong.360.cn/Loo/index/p/{0}.html"
        self.f = "{0}.txt"
        self.q_u = Queue()
        self.q_f = Queue()
        for i in xrange(1, 4619):
            self.q_u.put(self.u.format(i))
            self.q_f.put(self.f.format(i))


    def fetch_urls_and_save_to_file(self, url_queue, file_queue, element):
        try:
            while not url_queue.empty():
                url = url_queue.get()   #从url_queue中取出一个url
                file = file_queue.get()  #从file_queue中取出一个file
                doc = pq(url)
                ele = doc(element)    # 得到某个element的元素对象
                print "[*] " + url + " -> " + file    # 准备写入文件
                with open(file, 'w') as f:
                    count = 30
                    for j in ele.items(element):
                        f.write(j.text().encode('utf-8') + '\n')
                        count=count-1
                        if count == 0:
                            break
        except KeyboardInterrupt:
            pass



    def start(self, element):
        # 处理所有URL,开启5个线程
        gevent_list = []
        for index in range(2):
            gevent_list.append(
                gevent.spawn(self.fetch_urls_and_save_to_file, self.q_u, self.q_f, element)
            )
        gevent.joinall(gevent_list)


if __name__ == '__main__':
    downloader = ButianDownloader()
    downloader.start('dd')
