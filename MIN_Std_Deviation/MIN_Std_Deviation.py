# -*- coding: utf-8 -*-
"""
@author: Drapor

Description:
Calculate standard deviation of minutes played of each team of NBA 's lineups

"""

import re
import urllib2
import datetime
import sys

url='https://nba.hupu.com/teams/'
url_team=''
pattern = r'(?<=https://nba.hupu.com/teams/).*?(?=")'
pattern_time = r'(?<=<span class="c5">).*?(?=</span>)'
teampattern = r'(?<="name":").*?(?=")'
                 
request = urllib2.Request(url)
response = urllib2.urlopen(request)
content = response.read()
content = content.replace('\n','')
teamlist=re.findall(pattern,content)

teamlist={}.fromkeys(teamlist).keys()
teamlist.sort()


dict2={}

idx=2
t=1
teamdict={}


print 'Crawling data...'
for team in teamlist:
    print t,'/30...'
    t+=1
    time=[]
    avg_time=0.0
    variance =0.0
    url_team = url+team
    
    subrequest = urllib2.Request(url_team)
    subresponse = urllib2.urlopen(subrequest)
    subcontent = subresponse.read()
    subcontent = subcontent.replace('\n','')
    
    q=len(re.findall('c1',subcontent))-1
    
    subresult=re.findall(pattern_time, subcontent)
    subresult = subresult[20:]
    for i in range(q):
        time.append(subresult[idx+i*20])
    
    time = [float(x) for x in time]
    avg_time = sum(time)/q
    
    for i in time:
#        print i
        variance += (i-avg_time)**2
                   
    variance/=q
    teamdict[team]=round(variance**(0.5),3)

print 'Crawling Finished!'
dict= sorted(teamdict.iteritems(), key=lambda d:d[1], reverse = False)

teamlist.pop(0)
teamlist.remove('mavericks')
teamlist.insert(0,'sixers')

gurl="http://www.nba.com/"
fullname=[]
print 'Loading the full name of each teams...'


for team in teamlist:
    sys.stdout.write('#')
    request=urllib2.Request(gurl+team)
    response=urllib2.urlopen(request)
    content=response.read()
    fullname.append(re.findall(teampattern,content)[0])
    
fullname.insert(16,'Dallas Mavericks')

teamlist.insert(16,'mavericks')
teamlist.pop(0)
teamlist.insert(0,'76ers')

for i in range(30):
    dict2[teamlist[i]]=fullname[i]


print 'Up to',datetime.date.today().strftime("%Y-%m-%d"),',the rank is:'

for i in range(30):
    print '\t',dict2[dict[i][0]]

