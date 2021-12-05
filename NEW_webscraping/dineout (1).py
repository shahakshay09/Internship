#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[2]:


import requests
from bs4 import BeautifulSoup


# In[3]:


page=requests.get('https://www.dineout.co.in/delhi-restaurants/buffet-special')

page


# In[4]:


soup=BeautifulSoup(page.content)
soup


# In[10]:


first_name=soup.find('div',class_="restnt-info cursor")
first_name


# In[11]:


first_name.text


# In[13]:


first_name.text.split('|')[0]


# In[14]:


cuisine1=soup.find('span',class_="double-line-ellipsis")
cuisine1


# In[15]:


cuisine1.text


# In[17]:


cuisine1.text.split('|')[1]


# In[18]:


loc=soup.find('div',class_="restnt-loc ellipsis")
loc


# In[19]:


loc.text


# In[21]:


rating1=soup.find('div',class_="restnt-rating rating-4")
rating1


# In[22]:


rating1.text


# In[23]:


img=soup.find('img',class_="no-img")
img


# In[26]:


Restaurant_name=[]
for i in soup.find_all('div',class_="restnt-info cursor"):
    Restaurant_name.append(i.text)
Restaurant_name


# In[34]:


cuisine=[]
for i in soup.find_all('span',class_="double-line-ellipsis"):
    cuisine.append(i.text.split('|')[1])
cuisine


# In[37]:


location=[]
for i in soup.find_all('div',class_="restnt-loc ellipsis"):
    location.append(i.text)
location


# In[39]:


rating=[]
for i in soup.find_all('div',class_="restnt-rating rating-4"):
    rating.append(i.text)
rating


# In[5]:


img_url=[]
for i in soup.find_all('img',class_="no-img"):
    img_url.append(i['data-src'])
img_url


# In[41]:


print(len(Restaurant_name),len(cuisine),len(location),len(rating),len(img_url))


# In[42]:


import pandas as pd


# In[44]:


df = pd.DataFrame({'Restaurant_name':Restaurant_name,'cuisine':cuisine,'Location':location,'rating':rating,'Img_url':img_url})
df


# In[ ]:




