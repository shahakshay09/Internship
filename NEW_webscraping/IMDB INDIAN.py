#!/usr/bin/env python
# coding: utf-8

# In[52]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[53]:


import requests
from bs4 import BeautifulSoup


# In[54]:


page = requests.get('https://www.imdb.com/india/top-rated-indian-movies/?sort=ir,desc&mode=simple&page=1')
print(page)


# In[69]:


soup = BeautifulSoup(page.content, "html.parser")
print(soup)


# In[72]:


name = soup.find_all('td', class_="titleColumn")
print(name)


# In[77]:


movies = []
for movie in name:
    movie = movie.get_text().replace('\n',"  ")
    movie = movie.strip(" ")
    movies.append(movie)
print(movies)


# In[78]:


Rating =soup.find_all('td',class_="ratingColumn imdbRating")
rating


# In[87]:


ratings = []
for rating in Rating:
    rating = rating.get_text().replace('\n',"  ")
    ratings.append(rating)
print(ratings)


# In[105]:


year= soup.find_all('span',class_="secondaryInfo")
year


# In[100]:


print(len(movies),len(ratings),len(year))


# In[101]:


import pandas as pd


# In[103]:


df = pd.DataFrame({'movies':movies,'ratings':ratings,'year':year})
df


# In[ ]:




