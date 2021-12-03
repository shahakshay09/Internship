#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[2]:


import requests
from bs4 import BeautifulSoup


# In[3]:


page = requests.get("https://www.icc-cricket.com/rankings/womens/team-rankings/odi")
page


# In[4]:


soup = BeautifulSoup(page.content, 'html.parser')
soup


# In[5]:


team = soup.find('span',class_="u-hide-phablet")
team


# In[6]:


team=[]
for i in soup.find_all('span',class_="u-hide-phablet")[0:10]:
    team.append(i.text)
team


# In[7]:


matches1 = soup.find('td',class_="rankings-block__banner--matches")
print(matches1)


# In[43]:


matches1=[]
for i in soup.find_all('td',class_="rankings-block__banner--matches"):
    matches1.append(i.text)
    print(matches1)

     


# In[9]:


matches2 = soup.find('td',class_="table-body__cell u-center-text")
print(matches2)


# In[44]:


matches2 = []
for i in soup.find_all('td',class_="table-body__cell u-center-text")[0:9]:
    matches2.append(i.text)
    print(matches2)


# In[45]:


Match = matches1+matches2
print(Match)


# In[26]:


rating2 =soup.find('td',class_="rankings-block__banner--rating u-text-right")
rating2


# In[28]:


rating2 = []
for i in soup.find_all('td',class_="rankings-block__banner--rating u-text-right"):
    rating2.append(i.text)
    print(rating2)


# In[17]:


rating1= soup.find('td',class_="table-body__cell u-text-right rating")
print(rating1)


# In[39]:


rating1 = []
for i in soup.find_all('td',class_="table-body__cell u-text-right rating")[0:9]:
    rating1.append(i.text)
print(rating1)


# In[40]:


Rating = rating2+rating1
print(Rating)


# In[46]:


print(len(Match),len(team),len(Rating))


# In[47]:


import pandas as pd


# In[49]:


df = pd.DataFrame({'team':team,'Match':Match,'Rating':Rating})
print(df)


# In[50]:


##TOP ODI PLAYER###
players_page = requests.get("https://www.icc-cricket.com/rankings/womens/player-rankings/odi")
players_page


# In[52]:


soup=BeautifulSoup(players_page.content,"html.parser")
soup


# In[54]:


player1 = soup.find('div',class_="rankings-block__banner--name")
print(player1)


# In[57]:


player1 = []
for i in soup.find_all('div',class_="rankings-block__banner--name")[:1]:
    player1.append(i.text)
    print(player1)


# In[58]:


player2 = soup.find_all('td',class_="table-body__cell name")
print(player2)


# In[59]:


player2 = []
for i in soup.find_all('td',class_="table-body__cell name")[0:9]:
    player2.append(i.text)
    print(player2)


# In[60]:


Players = player1+player2
print(Players)


# In[86]:


team1 = soup.find('div',class_="rankings-block__banner--nationality")
print(team1)


# In[87]:


team1=[]
for i in soup.find_all('div',class_="rankings-block__banner--nationality")[:1]:
    team1.append(i.text)
    print(team1)


# In[76]:


team2 = soup.find('span',class_="table-body__logo-text")
print(team2)


# In[80]:


team2 = []
for i in soup.find_all('span',class_="table-body__logo-text")[18:30]:
    team2.append(i.text)
    print(team2)


# In[83]:


Team = team1+team2
print(Team)


# In[88]:


rating1 = soup.find('div',class_="rankings-block__banner--rating")
rating1


# In[92]:


rating1 = []
for i in soup.find_all('div',class_="rankings-block__banner--rating")[0]:
    rating1.append(i)
    print(rating1)


# In[93]:


rating2 = soup.find('td',class_="table-body__cell u-text-right rating")
rating2


# In[95]:


rating2=[]
for i in soup.find_all('td',class_="table-body__cell u-text-right rating")[0:9]:
    rating2.append(i.text)
    print(rating2)


# In[96]:


Rating = rating1+rating2
print(Rating)


# In[98]:


womens_player_df = pd.DataFrame({'Players':Players,'Team':Team,'Rating':Rating})
print(womens_player_df)


# In[99]:


#####TOP ODI WOMENS ALLROUNDER###

allrounder = soup.find('div',class_="rankings-block__banner--name")
print(allrounder)


# In[108]:


allrounder1 = []
for i in soup.find_all('div',class_="rankings-block__banner--name")[2]:
    allrounder1.append(i)
    print(allrounder1)


# In[104]:


allrounder2 = soup.find('td',class_="table-body__cell name")
print(allrounder2)


# In[110]:


allrounder2 = []
for i in soup.find_all('td',class_="table-body__cell name")[18:30]:
    allrounder2.append(i.text)
    print(allrounder2)


# In[111]:


Allrounder = allrounder1+allrounder2
print(Allrounder)


# In[122]:


team1 = soup.find('div',class_="rankings-block__banner--nationality")
print(team1)


# In[128]:


team1 = []
for i in soup.find_all('div',class_="rankings-block__banner--nationality")[:1]:
    team1.append(i.text)
    print(team1)


# In[129]:


team2 = soup.find('span',class_="table-body__logo-text")
print(team2)


# In[130]:


team2 = []
for i in soup.find_all('span',class_="table-body__logo-text")[18:30]:
    team2.append(i.text)
    print(team2)


# In[146]:


Team=team1+team2
print(Team)


# In[133]:


Rating = soup.find('td',class_="table-body__cell u-text-right rating")
Rating


# In[135]:


Rating = []
for i in soup.find_all('td',class_="table-body__cell u-text-right rating")[18:30]:
    Rating.append(i.text)
    print(Rating)


# In[144]:


Rating[0:1] = ('384'),('372')


# In[145]:


print(Rating)


# In[147]:


print(len(Allrounder),len(Team),len(Rating))


# In[150]:


Allrounder_df = pd.DataFrame({'Allrounder':Allrounder,'Team':Team,'Rating':Rating})
print(Allrounder_df)


# In[ ]:




