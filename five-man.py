# -*- coding: utf-8 -*-
"""
My First Crawler!!!So excited!!!

@author: Drapor
"""
import re
import urllib2

head='<!DOCTYPEhtml><html><head><title>FiveManStat</title></head><body><center\
><h1>Crawl From 82games.com</h1><h5>by Drapor</h5></center><hr>'

url_raw='http://www.82games.com/index.htm'

startpattern=r'<Table width=520.*?</table>'
subpattern=r'<td><font face=verdana size=-1>.*?</table>.*?</table>'
pattern = r'(?<=<a href=").*(?=">)'
rubpattern=r'<A href=".*By Position</font></u></a><p>'

rub='<center><font face=verdana size=-1>We want your feedback!<a href="http://\
www.82games.com/contact.htm">Tell us your thoughts</a> </center>'


#First Layer
request = urllib2.Request(url_raw)
response = urllib2.urlopen(request)
content = response.read()
result = re.findall(pattern,content)
result=result[4:34]
#result=result[4:7]
f=open('index.html','w')
f.write(head)

t=0.0
for sites in result:
    url=sites.replace('.HTM','2.HTM')
    t+=1
    print sites[-7:-4]
    subrequest = urllib2.Request(url)
    subresponse = urllib2.urlopen(subrequest)
    subcontent = subresponse.read()
    subcontent = subcontent.replace('\n','')
    subresult = re.findall(subpattern,subcontent)
    
    if result.index(sites)==0:
        legend=re.findall(startpattern,subcontent)
        legend[0]=legend[0].replace('Legend:','')
        f.write('<center>'+legend[0]+'<hr>')
    else:
        pass    

    if len(subresult)!=0:
        sub=re.sub(rubpattern, r'<br>', subresult[0])
        f.write('<center>'+sub.replace(rub,'')+'</center>'+'<hr>')
    else:
        pass
    
    
    f.write('\n')

print 'Finished!Yeah!'
f.close()
    