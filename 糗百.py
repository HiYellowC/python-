# -*- coding: UTF-8 -*-
import urllib
import urllib2
import re
 
page = 5
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
request = urllib2.Request(url,headers = headers)
response = urllib2.urlopen(request)
res = re.compile('author clearfix[\s|\S]*?alt="(.*?)"[\s|\S]*?content">\n\n(.*?)\n<!--[\s|\S]*?number">(\d+)</i>')

ans = re.findall(res, response.read())

dex = 1

for e in ans:
    print dex, '.'
    print '作者', e[0]
    print '内容', e[1]
    print '人气', e[2], '\n'
    dex += 1

