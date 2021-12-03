#!/usr/bin/env python
# coding: utf-8

# In[27]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[28]:


import requests
from bs4 import BeautifulSoup


# In[29]:


page=requests.get('https://en.tutiempo.net/delhi.html?data=last-24-hours')
page


# In[30]:


soup=BeautifulSoup(page.content, 'html.parser')
soup


# In[100]:


hour = soup.find('td',class_="")
print(hour)


# In[116]:


hour = []
for i in soup.find_all('td',class_='t Temp')[0:24]: 

    if i.previous_sibling.previous_sibling is not None:

        hour.append(i.previous_sibling.previous_sibling.text)

    else:

        hour.append(' ')


# In[117]:


print(hour)


# In[80]:


temperature = soup.find('td', class_="t Temp")
temperature


# In[81]:


temperature.text


# In[82]:


wind = soup.find('td',class_="wind")
wind


# In[83]:


wind.text


# In[131]:


weather = soup.find('span')
print(weather)


# In[132]:


weather = []
for i in soup.find_all('td',class_='t Temp')[0:24]: 

    if i.previous_sibling is not None:

        weather.append(i.previous_sibling.text)

    else:

        weather.append(' ')


# In[133]:


print(weather)


# In[86]:


humidity = soup.find('td',class_="hr")
humidity


# In[87]:


humidity.text


# In[88]:


pressure = soup.find('td',class_="prob")
pressure


# In[89]:


pressure.text


# In[123]:


temperature=[]
for i in soup.find_all('td',class_="t Temp")[0:24]:
    temperature.append(i.text)
print(temperature)


# In[122]:


wind=[]
for i in soup.find_all('td',class_="wind")[0:24]:
    wind.append(i.text)
wind


# In[121]:


humidity=[]
for i in soup.find_all('td',class_="hr")[0:24]:
    humidity.append(i.text)
humidity


# In[119]:


pressure=[]
for i in soup.find_all('td',class_="prob")[0:24]:
    pressure.append(i.text)
pressure


# In[135]:


print(len(hour),len(temperature),len(wind),len(weather),len(humidity),len(pressure))


# In[107]:


import pandas as pd


# In[136]:


df = pd.DataFrame({'hour':hour,'temperature':temperature,'wind':wind,'weather':weather,'humidity':humidity,'pressure':pressure})
df


# In[ ]:




