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


# In[9]:


womens_list = soup.find_all('td',class_="table-body__cell u-center-text")
print(womens_list)


# In[10]:


Match=[]
Points=[]
for i in soup.find_all('td',class_="rankings-block__banner--matches"):
   womens_list.append(i.text)
for i in range(0,len(womens_list)-1,2):
    Match.append(womens_list[i])
    Points.append(womens_list[i+1])
 

     


# In[11]:


print(Match)


# In[14]:


print(Points)


# In[38]:


Rating= soup.find('td',class_="table-body__cell u-text-right rating")
print(Rating)


# In[39]:


Rating = []
for i in soup.find_all('td',class_="table-body__cell u-text-right rating"):
    Rating.append(i.text)
print(Rating)


# In[40]:


print(len(Match),len(Points),len(team),len(Rating))


# In[41]:


import pandas as pd


# In[42]:


womens_top = pd.DataFrame({'team':team,'Match':Match,'Points':Points,'Rating':Rating})


# In[43]:


print(womens_top)


# In[44]:


##TOP ODI PLAYER###
players_page = requests.get("https://www.icc-cricket.com/rankings/womens/player-rankings/odi")
players_page


# In[45]:


soup=BeautifulSoup(players_page.content,"html.parser")
soup


# In[46]:


player1 = soup.find('div',class_="rankings-block__banner--name")
print(player1)


# In[47]:


player1 = []
for i in soup.find_all('div',class_="rankings-block__banner--name")[:1]:
    player1.append(i.text)
    print(player1)


# In[48]:


player2 = soup.find_all('td',class_="table-body__cell name")
print(player2)


# In[49]:


player2 = []
for i in soup.find_all('td',class_="table-body__cell name")[0:9]:
    player2.append(i.text)
    print(player2)


# In[50]:


Players = player1+player2
print(Players)


# In[51]:


team1 = soup.find('div',class_="rankings-block__banner--nationality")
print(team1)


# In[52]:


team1=[]
for i in soup.find_all('div',class_="rankings-block__banner--nationality")[:1]:
    team1.append(i.text)
    print(team1)


# In[53]:


team2 = soup.find('span',class_="table-body__logo-text")
print(team2)


# In[54]:


team2 = []
for i in soup.find_all('span',class_="table-body__logo-text")[18:30]:
    team2.append(i.text)
    print(team2)


# In[55]:


Team = team1+team2
print(Team)


# In[56]:


rating1 = soup.find('div',class_="rankings-block__banner--rating")
rating1


# In[57]:


rating1 = []
for i in soup.find_all('div',class_="rankings-block__banner--rating")[0]:
    rating1.append(i)
    print(rating1)


# In[58]:


rating2 = soup.find('td',class_="table-body__cell u-text-right rating")
rating2


# In[59]:


rating2=[]
for i in soup.find_all('td',class_="table-body__cell u-text-right rating")[0:9]:
    rating2.append(i.text)
    print(rating2)


# In[60]:


Rating = rating1+rating2
print(Rating)


# In[61]:


womens_player_df = pd.DataFrame({'Players':Players,'Team':Team,'Rating':Rating})
print(womens_player_df)


# In[62]:


#####TOP ODI WOMENS ALLROUNDER###

allrounder = soup.find('div',class_="rankings-block__banner--name")
print(allrounder)


# In[63]:


allrounder1 = []
for i in soup.find_all('div',class_="rankings-block__banner--name")[2]:
    allrounder1.append(i)
    print(allrounder1)


# In[64]:


allrounder2 = soup.find('td',class_="table-body__cell name")
print(allrounder2)


# In[65]:


allrounder2 = []
for i in soup.find_all('td',class_="table-body__cell name")[18:30]:
    allrounder2.append(i.text)
    print(allrounder2)


# In[66]:


Allrounder = allrounder1+allrounder2
print(Allrounder)


# In[67]:


team1 = soup.find('div',class_="rankings-block__banner--nationality")
print(team1)


# In[68]:


team1 = []
for i in soup.find_all('div',class_="rankings-block__banner--nationality")[:1]:
    team1.append(i.text)
    print(team1)


# In[69]:


team2 = soup.find('span',class_="table-body__logo-text")
print(team2)


# In[70]:


team2 = []
for i in soup.find_all('span',class_="table-body__logo-text")[18:30]:
    team2.append(i.text)
    print(team2)


# In[71]:


Team=team1+team2
print(Team)


# In[72]:


Rating = soup.find('td',class_="table-body__cell u-text-right rating")
Rating


# In[73]:


Rating = []
for i in soup.find_all('td',class_="table-body__cell u-text-right rating")[18:30]:
    Rating.append(i.text)
    print(Rating)


# In[74]:


Rating[0:1] = ('384'),('372')


# In[75]:


print(Rating)


# In[76]:


print(len(Allrounder),len(Team),len(Rating))


# In[77]:


Allrounder_df = pd.DataFrame({'Allrounder':Allrounder,'Team':Team,'Rating':Rating})
print(Allrounder_df)


# In[ ]:





# In[ ]:




