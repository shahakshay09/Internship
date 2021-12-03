#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[2]:


import requests
from bs4 import BeautifulSoup


# In[3]:


page=requests.get('https://coreyms.com/')

page


# In[4]:


soup=BeautifulSoup(page.content)
soup


# In[5]:


heading = soup.find('h2',class_="entry-title")
heading


# In[6]:


heading.text


# In[7]:


date = soup.find('time',class_="entry-time")
date


# In[8]:


date.text


# In[74]:


content = soup.find('div',class_="entry-content")
content


# In[75]:


content.text


# In[123]:


video_link = soup.find('iframe',class_="youtube-player")['src']
video_link


# In[124]:


video_link = []
for i in soup.find_all('iframe',class_="youtube-player"):
    video_link.append(i['src'])
video_link


# In[101]:


heading = []
for i in soup.find_all('h2',class_="entry-title"):
    heading.append(i)
print(heading)


# In[60]:


date = []
for i in soup.find_all('time',class_="entry-time"):
    date.append(i.text)
print(date)


# In[77]:


content = []
for i in soup.find_all('div',class_="entry-content"):
    content.append(i.text)
print(content)


# In[94]:


print(len(heading),len(date),len(content),len(video_link))


# In[105]:


import pandas as pd


# In[108]:


df = pd.DataFrame({'heading':heading,'date':date,'content':content,})
df


# In[119]:


df.index=['1','2','3','4','(5)','5','6','7','8','9']


# In[120]:


df


# In[128]:


dataset = df.drop("(5)",axis="index")


# In[129]:


dataset


# In[131]:


dataset['video_links'] = video_link


# In[132]:


dataset


# In[ ]:




