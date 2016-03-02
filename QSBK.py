# -*- coding: UTF-8 -*-
import urllib
import urllib2
import os
import re
 
class QSBK:

    def init(self):
        self.page = 1
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = { 'User-Agent' : self.user_agent }
    
    def load(self):
        url = 'http://www.qiushibaike.com/hot/page/' + str(self.page)
        request = urllib2.Request(url,headers = self.headers)
        response = urllib2.urlopen(request)
        res = re.compile('author clearfix[\s|\S]*?alt="(.*?)"[\s|\S]*?content">\n\n(.*?)\n<!--([\s|\S]*?)number">(\d+)</i>')
        self.ans = re.findall(res, response.read())
        self.page += 1

    def show(self):
        self.init()
        dex = 1
        i = 'x'
        while i != 'q':
            self.load()
            for e in self.ans:
                if re.search('img', e[2]): 
                    continue
                os.system('clear')
                print dex, '.'
                print '作者:', e[0]
                print '内容:', e[1]
                print '人气:', e[3], '\n'
                i = raw_input()
                if i == 'q': 
                    break
                dex += 1

q = QSBK()
q.show()
