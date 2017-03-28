# -*- coding: utf-8 -*-
"""
Exercise 0 : http://www.heibanke.com/lesson/crawler_ex01/

@author: Drapor
"""
import re
import urllib
import urllib2

url='http://www.heibanke.com/lesson/crawler_ex01/'
n=1
headers={ 'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
pattern=r'密码错误'
while(1):
    value={'username':'Drapor','password':n}
    data = urllib.urlencode(value)
    request=urllib2.Request(url,data,headers) 
    #you should use this rather than 'response=response=urllib2.urlopen(url,data,headers),
    #or you will get 'TypeError: a float is required'
    response=urllib2.urlopen(request)
    content = response.read()
    result=re.findall(pattern,content)
    if len(result)==0:
        print '对啦，应该是',n
        break
    else:
        print 'n=',n,result[0]
        n+=1
#print content
