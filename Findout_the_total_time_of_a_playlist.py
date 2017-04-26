# -*- coding: utf-8 -*-
"""
Date:17.4.26
Description:
    打算开始上机器学习基石了，但不知道这个课总共有多久，于是写了这个，原谅我的懒……
    计算结果是15:30:54
@author: Drapor
"""
import re
import urllib2


url='https://www.youtube.com/playlist?list=PLXVfgk9fNX2I7tB6oIINGBmW50rrmFTqf'
request = urllib2.Request(url)
response = urllib2.urlopen(request)
content = response.read()
content = content.replace('\n','')
m=0
s=0
h=0
pattern = r'\d{1,2}:\d{1,2}'
                 

result=re.findall(pattern,content)

for i in result:
    m+=int(i[:-3])
    s+=int(i[-2:])
    
m+=s/60
s=s%60
h+=m/60
m=m%60

str(h)+':'+str(m)+':'+str(s)