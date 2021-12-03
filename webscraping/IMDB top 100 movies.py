#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[2]:


import requests
from bs4 import BeautifulSoup


# In[3]:


page=requests.get('https://www.imdb.com/list/ls091520106/')
page


# In[5]:


soup=BeautifulSoup(page.content)
print(soup)


# In[12]:


titles1 = soup.find('h3', class_="lister-item-header")
titles1


# In[13]:


titles1.text


# In[39]:


rating = soup.find('div',class_="ipl-rating-widget").find_all('div')
rating


# In[23]:


year = soup.find('span', class_="lister-item-year text-muted unbold")
print(year)


# In[24]:


year.text


# In[25]:


#multipy scraping
titles = []
for i in soup.find_all('h3', class_="lister-item-header"):
    titles.append(i.text)
print(titles)


# In[41]:


rating = []
for i in soup.find_all('div', class_="ipl-rating-widget"):
    rating.append(i.text)
print(rating)
    


# In[29]:


year = []
for i in soup.find_all('span', class_="lister-item-year text-muted unbold"):
    year.append(i.text)
print(year)


# In[42]:


#cheching len
print(len(titles),len(rating),len(year))


# In[43]:


import pandas as pd


# In[55]:


df = pd.DataFrame({'titles':titles,'rating':rating,'year':year})
df


# In[58]:


for column in df.columns:
    df[column] =df[column].str.replace(r'\W'," ",regex=True) 
print(df)


# In[59]:


df.head()


# In[60]:


df


# In[ ]:




