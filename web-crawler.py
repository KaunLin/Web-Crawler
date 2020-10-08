
# coding: utf-8

# In[1]:

import requests
import json
url="https://www.mobile01.com/topiclist.php?f=383"
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
a = requests.get(url,headers=headers)
#a.text


# In[2]:

from bs4 import BeautifulSoup
net=BeautifulSoup(a.text, 'html.parser')
tag_name = 'span.subject-text a'
articles = net.select(tag_name)
#articles


# In[3]:

domain = 'https://www.mobile01.com/'
for art in articles:
    print(domain + art.get('href'))


# In[10]:

from bs4 import BeautifulSoup
url="https://www.mobile01.com/topicdetail.php?f=383&t=5672605"
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
topic = requests.get(url,headers=headers)
topicc = BeautifulSoup(topic.text,'lxml')
print ("標題:"+topicc.select('.topic')[0].text)
print (topicc.select('.info')[0].text)
print ("時間:"+topicc.select('.date')[0].text)
pointword='.fn'
for ta in topicc.select(pointword)[0]:
    print("作者ID:"+(ta.text))
    break
contentpoint ='div[id^=ct]'
content = topicc.select(contentpoint)
print("內文:\n"+(content)[0].text)


# In[5]:

for tb in topicc.select(pointword):
    if tb == topicc.select(pointword)[0]:
        continue;
    else:
        print("回覆者ID:"+(tb.text))


# In[8]:

for tc in topicc.select('.date'):
    if tc == topicc.select('.date')[0]:
        continue
    else:
        print ("時間:"+tc.text)


# In[22]:

for td in topicc.select(contentpoint):
    if td == topicc.select(contentpoint)[0]: 
        continue
    else:
        print(("內容:"+(td)[0].text)


# In[13]:

for tf in topicc:
    for tb in topicc.select(pointword):
        if tb == topicc.select(pointword)[0]:
            continue;
        else:
            print("回覆者ID:"+(tb.text))
    for tc in topicc.select('.date'):
        if tc == topicc.select('.date')[0]:
            continue;
        else:
            print ("時間:"+tc.text)
    for td in topicc.select(contentpoint):
        if td == topicc.select(contentpoint)[0]: 
            continue
        else:
            print("內容:"+td.text)
    


# In[ ]:



