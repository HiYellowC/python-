# -*- coding: UTF-8 -*-
import urllib
import urllib2
from PIL import Image
from StringIO import StringIO
from io import BytesIO

class QDJW:

    def __init__(self):
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip,deflate,sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': 'JSESSIONID=E94969BA093F1BBAD96594300BD22183.TAC2; _gscu_1067863974=5077358605kwkn49; _ga=GA1.3.546663490.1456995230; __utmt=1; __utma=50352818.546663490.1456995230.1457054375.1457074402.4; __utmb=50352818.2.10.1457074402; __utmc=50352818; __utmz=50352818.1456995299.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
            'Host': 'jw.qdu.edu.cn',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36'
        }
    
    def getPage(self, index):
        url = 'http://jw.qdu.edu.cn/academic/student/studentinfo/loadphoto_added.jsdo?primary=userid&kind=student&userid=' + str(index)
        request = urllib2.Request(url, headers = self.headers)
        self.response = urllib2.urlopen(request)
        if self.response.url == 'http://jw.qdu.edu.cn/academic/common/security/login.jsp':
            print '请更换cookie'
            sys.exit(0)

    def fileSave(self, index):
        jpg = Image.open(BytesIO(self.response.read()))
        if jpg.size != (90, 120):
            jpg.save('pic/' + str(index) + '.jpg')
            print '成功写入' + str(index) + '.jpg'

    def start(self, first, last, step):
        while first <= last:
            self.getPage(first)
            self.fileSave(first)
            first += step

qdjw = QDJW()
qdjw.start(1, 1, 1)
