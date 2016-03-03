# -*- coding: UTF-8 -*-
import urllib
import urllib2
import os
import re

class BDTB:

    def __init__(self, inputURL, inputLZ):
        self.url = inputURL + '?see_lz=' + inputLZ
        userAgent = {'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36'}
        self.headers = {'User-Agent': userAgent}
        self.file = open('BDTB.txt', 'w')
        self.contentIndex = 1
    
    def getPage(self, pageIndex):
        self.url = self.url + '&pn=' + pageIndex 
        self.request = urllib2.Request(self.url, headers = self.headers)
        self.response = urllib2.urlopen(self.request)

    def getInf(self):
        page = self.response.read()
        self.maxPage = re.search('max-page="(\d+)"', page)
        self.title = re.search('<title>(.*?)</title>', page)
        self.content = re.findall('"d_post_content j_d_post_content ">(.*?)<div class="user-hide-post-down"', page)

    def formatInf(self):
        self.formatContent = []
        for c in self.content:
            cc = re.sub(' ', '', c)
            self.formatContent.append(re.sub('<.*?>', '\n', cc))

    def inputFile(self, pageIndex):
        print '正在写入第%d页数据' %pageIndex
        if pageIndex == 1:
            self.file.writelines(self.title.group(1))
        for x in self.formatContent:
            self.file.writelines('\n---------------------------------------' 
                                 + str(self.contentIndex) 
                                 + '---------------------------------------\n')
            self.file.writelines(x)
            self.contentIndex += 1

    def start(self):
        pageIndex = 1
        while True:
            self.getPage(str(pageIndex))
            self.getInf()
            if pageIndex == 1:
                if self.maxPage == None: print '该贴共有1页', 
                else: print '该贴共有%d页' %int(self.maxPage.group(1))
            self.formatInf()
            self.inputFile(pageIndex)
            pageIndex += 1
            if self.maxPage == None or pageIndex > int(self.maxPage.group(1)):
                break
        print '写入任务完成'
        self.file.close()

inputURL = raw_input('请输入贴吧域名：')
inputLZ = raw_input('是否只获取楼主发言，是输入1,否输入0：')
b = BDTB(inputURL, inputLZ)
b.start()


