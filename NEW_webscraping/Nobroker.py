#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[2]:


import requests
from bs4 import BeautifulSoup


# In[3]:


page = requests.get("https://www.nobroker.in/property/sale/bangalore/Electronic%20City?type=BHK4&searchParam=W3sibGF0IjoxMi44N%20DUyMTQ1LCJsb24iOjc3LjY2MDE2OTUsInBsYWNlSWQiOiJDaElKdy1GUWQ0cHNyanNSSGZkYXpnXzhYRW8%20iLCJwbGFjZU5hbWUiOiJFbGVjdHJvbmljIENpdHkifV0=&propertyAge=0&radius=2.0")
page


# In[4]:


soup=BeautifulSoup(page.content, "html.parser")
soup


# In[5]:


house_title = soup.find('h2', class_="heading-6 font-semi-bold nb__25Cl7")
house_title.text


# In[6]:


location = soup.find('div', class_="nb__1EwQz")
location.text


# In[7]:


Area = soup.find('div', class_="nb__FfHqA")
Area.text


# In[15]:


emi = soup.find('div',id="roomType")
emi.text


# In[27]:


price = soup.find('div',id="minDeposit")
price.text.split('|')


# In[17]:


house_title = []
for i in soup.find_all('h2', class_="heading-6 font-semi-bold nb__25Cl7")[0:16]:
    house_title.append(i.text)
print(house_title)


# In[18]:


location = []
for i in soup.find_all('div', class_="nb__1EwQz")[0:16]:
    location.append(i.text)
print(location)


# In[19]:


Area = []
for i in soup.find_all('div', class_="nb__FfHqA")[0:16]:
    Area.append(i.text)
print(Area)


# In[20]:


emi = []
for i in soup.find_all('div',id="roomType")[0:16]:
    emi.append(i.text)
print(emi)


# In[35]:


price = []
for i in soup.find_all('div',id="minDeposit")[0:16]:
    price.append(i.text)
print(price)


# In[29]:


print(len(house_title),len(location),len(Area),len(emi),len(price))


# In[30]:


import pandas as pd


# In[36]:


df = pd.DataFrame({'house_title':house_title,'location':location,'Area':Area,'emi':emi,'price':price})
df


# In[ ]:




