#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[ ]:





# In[2]:


import requests
from bs4 import BeautifulSoup


# In[3]:


page = requests.get('https://en.wikipedia.org/wiki/Main_Page')
print(page)


# In[4]:


soup = BeautifulSoup(page.content)
print(soup)


# In[5]:


header = soup.find('span',class_="mw-headline")
print(header)


# In[6]:


header.text


# In[7]:


header = []
for i in soup.find_all('span',class_="mw-headline"):
    header.append(i.text)
print(header)


# In[8]:


import pandas as pd


# In[9]:


df = pd.DataFrame({'header':header})
print(df)


# In[ ]:




