#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[2]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[3]:


page = requests.get('https://www.icc-cricket.com/rankings/mens/team-rankings/odi')
page


# In[4]:


soup=BeautifulSoup(page.content, "html.parser")
soup


# In[5]:


Team = soup.find('span', class_="u-hide-phablet")
Team.text


# In[6]:


matches = soup.find_all('td',class_="table-body__cell u-center-text")
matches


# In[21]:


matches = []
for i in soup.find_all('td',class_="table-body__cell u-center-text")[0:10]:
    matches.append(i.text)
print(matches)


# In[8]:


points = soup.find('td',class_="table-body__cell u-center-text")
points


# In[9]:


rating = soup.find('td',class_="table-body__cell u-text-right rating")
rating.text.replace('\n','')


# In[10]:


Team = []
for i in soup.find_all('span', class_="u-hide-phablet")[0:10]:
    Team.append(i.text)
print(Team)


# In[18]:


points = []
for i in soup.find_all('td',class_="table-body__cell u-center-text")[0:10]:
    points.append(i.text)
print(points)


# In[13]:


rating = []
for i in soup.find_all('td',class_="table-body__cell u-text-right rating")[0:10]:
    rating.append(i.text)
print(rating)


# In[22]:


print(len(Team),len(matches),len(points),len(rating))


# In[23]:


import pandas as pd


# In[24]:


df = pd.DataFrame({'Team':Team,'matches':matches,'points':points,'rating':rating})
df


# In[ ]:


#######program for top 10 ODI player####


# In[25]:


player_page = requests.get("https://www.icc-cricket.com/rankings/mens/player-rankings/odi")
player_page


# In[26]:


soup=BeautifulSoup(player_page.content, "html.parser")
soup


# In[27]:


player1 = soup.find('div',class_="rankings-block__banner--name")
print(player1)


# In[28]:


player1 = []
for i in soup.find_all('div',class_="rankings-block__banner--name")[0:1]:
    player1.append(i.text)
print(player1)


# In[29]:



player2 = soup.find('td',class_="table-body__cell name")
print(player2)


# In[30]:


player2 = []
for i in soup.find_all('td',class_="table-body__cell name")[0:9]:
    player2.append(i.text)
print(player2)


# In[32]:


player = player1 + player2
print(player)


# In[33]:


country = soup.find('span',class_="table-body__logo-text")
print(country)


# In[34]:


country = []
for i in soup.find_all('span',class_="table-body__logo-text")[0:10]:
    country.append(i.text)
    print(country)


# In[35]:


country[0]= 'PAK'
country[2]= 'IND'
print(country)


# In[36]:


rating = soup.find('td',class_="table-body__cell u-text-right rating")
print(rating)


# In[37]:


rating=[]
for i in soup.find_all('td',class_="table-body__cell u-text-right rating")[0:10]:
    rating.append(i.text)
    print(rating)


# In[38]:


rating[0]='873'
print(rating)


# In[39]:


print(len(player),len(country),len(rating))


# In[40]:


import pandas as pd


# In[41]:


df = pd.DataFrame({'player':player,'country':country,'rating':rating})
print(df)


# In[102]:


#####top 10 bowlers###


# In[49]:


soup = BeautifulSoup(bowler_page.content, "html.parser")
soup


# In[50]:


bowler_page = requests.get("https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling")
print(bowler_page)


# In[85]:


bowler1 = soup.find('div',class_="rankings-block__banner--name-large")
print(bowler)


# In[54]:


bowler1 = []
for i in soup.find_all('div',class_="rankings-block__banner--name-large"):
    bowler1.append(i.text)
    print(bowler1)


# In[55]:


bowler2 = soup.find('td',class_="table-body__cell rankings-table__name name")
print(bowler2)


# In[59]:


bowler2 = []
for i in soup.find_all('td',class_="table-body__cell rankings-table__name name")[0:9]:
    bowler2.append(i.text)
    print(bowler2)


# In[60]:


Bowlers = bowler1 + bowler2
print(Bowlers)


# In[61]:


team =soup.find('div',class_="rankings-block__banner--nationality")
print(team)


# In[66]:


team = []
for i in soup.find_all('div',class_="rankings-block__banner--nationality"):
    team.append(i.text)
    print(team)


# In[67]:


team1 = soup.find('span',class_="table-body__logo-text")
print(team1)


# In[69]:


team1 = []
for i in soup.find_all('span',class_="table-body__logo-text")[0:9]:
    team1.append(i.text)
    print(team1)


# In[70]:


Team = team+team1
print(Team)


# In[71]:


rating1 = soup.find('div',class_="rankings-block__banner--rating")
print(rating1)


# In[80]:


rating1 = []
for i in soup.find_all('div',class_="rankings-block__banner--rating"):
    rating1.append(i.text)
    print(rating1)


# In[72]:


rating2 = soup.find('td',class_="table-body__cell rating")
rating2


# In[73]:


rating2 = []
for i in soup.find_all('td',class_="table-body__cell rating")[0:9]:
    rating2.append(i.text)
    print(rating2)


# In[81]:


Rating = rating1+rating2
print(Rating)


# In[82]:


print(len(Bowlers),len(Team),len(Rating))


# In[84]:


bowlers_df = pd.DataFrame({'Bowlers':Bowlers,'Team':Team,'Rating':Rating})
print(bowlers_df)


# In[ ]:




