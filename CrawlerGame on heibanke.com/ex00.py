# -*- coding: utf-8 -*-
"""
Exercise 0 : http://www.heibanke.com/lesson/crawler_ex00/

@author: Drapor
"""
import re
import urllib2

url_raw='http://www.heibanke.com/lesson/crawler_ex00/'
pattern = r'(?<=数字是)\d{5}'    
num='64972'   #First number you see on the page.
while(1):
    url=url_raw+num
    response=urllib2.urlopen(url)
    content = response.read()
    result=re.findall(pattern,content)
    
    if len(result)==0:
        break
    else:
        print result[0] #Display the number on the page to help you realize the program is still running
        num=result[0]

print 'the final answer is',num


