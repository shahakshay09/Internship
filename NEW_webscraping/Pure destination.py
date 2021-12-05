#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[2]:


import requests
from bs4 import BeautifulSoup


# In[3]:


page=requests.get('https://www.puredestinations.co.uk/top-10-famous-monuments-to-visit-in-india/')
page


# In[4]:


soup=BeautifulSoup(page.content, "html.parser")
soup


# In[5]:


monument=soup.find('strong',class_=False)
monument


# In[6]:


monument.text


# In[7]:


monument=[]
for i in soup.find_all('strong',class_=False)[0:10]:
    monument.append(i.text)
monument


# In[97]:


description = soup.find_all('p')
description
    


# In[105]:


description = []
for i in soup.find_all('p',class_=False)[5:15]:
    description.append(i.text)
print(description)


# In[90]:


img = soup.find_all('img')
img


# In[111]:


img = []
for i in soup.find_all('img')[5:15]:
    img.append(i['src'])
img


# In[112]:


print(len(monument),len(description),len(img))


# In[100]:


import pandas as pd


# In[113]:


df = pd.DataFrame({'monument':monument,'description':description,'img':img})


# In[114]:


df


# In[ ]:




