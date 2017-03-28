# -*- coding: utf-8 -*-
"""
@author: Drapor

Description:
Calculate standard deviation of minutes played of each team of NBA 's lineups

"""
import re
import urllib2


url='https://nba.hupu.com/teams/'
url_team=''
pattern = r'(?<=https://nba.hupu.com/teams/).*?(?=")'
pattern_time = r'(?<=<span class="c5">).*?(?=</span>)'

                 
request = urllib2.Request(url)
response = urllib2.urlopen(request)
content = response.read()
content = content.replace('\n','')
teamlist=re.findall(pattern,content)

teamlist={}.fromkeys(teamlist).keys()
teamlist.sort()
idx=2
t=1
teamdict={}
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

print 'Finished!'
dict= sorted(teamdict.iteritems(), key=lambda d:d[1], reverse = False)