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


# In[65]:


soup=BeautifulSoup(page.content)
soup


# In[66]:


Team = soup.find('span', class_="u-hide-phablet")
Team.text


# In[101]:


mens_list = soup.find_all('td',class_="table-body__cell u-center-text")[0:18]
mens_list


# In[102]:


matches=[]
points = []


# In[103]:


for i in soup.find('td',class_="table-body__cell u-center-text"):  
    mens_list.append(i)
for i in range(0,len(mens_list)-1,2):
    matches.append(mens_list[i])
    points.append(mens_list[i+1])


# In[104]:


print(matches)


# In[105]:


print(points)


# In[24]:


rating = soup.find('td',class_="table-body__cell u-text-right rating")
rating.text.replace('\n','')


# In[107]:


Team = []
for i in soup.find_all('span', class_="u-hide-phablet")[0:9]:
    Team.append(i.text)
print(Team)


# In[108]:


rating = []
for i in soup.find_all('td',class_="table-body__cell u-text-right rating")[0:9]:
    rating.append(i.text)
print(rating)


# In[109]:


print(len(Team),len(matches),len(points),len(rating))


# In[110]:


import pandas as pd


# In[111]:


df = pd.DataFrame({'Team':Team,'matches':matches,'points':points,'rating':rating})
df


# In[112]:


#######program for top 10 ODI player####


# In[113]:


player_page = requests.get("https://www.icc-cricket.com/rankings/mens/player-rankings/odi")
player_page


# In[114]:


soup=BeautifulSoup(player_page.content, "html.parser")
soup


# In[115]:


player1 = soup.find('div',class_="rankings-block__banner--name")
print(player1)


# In[116]:


player1 = []
for i in soup.find_all('div',class_="rankings-block__banner--name")[0:1]:
    player1.append(i.text)
print(player1)


# In[117]:



player2 = soup.find('td',class_="table-body__cell name")
print(player2)


# In[118]:


player2 = []
for i in soup.find_all('td',class_="table-body__cell name")[0:9]:
    player2.append(i.text)
print(player2)


# In[119]:


player = player1 + player2
print(player)


# In[120]:


country = soup.find('span',class_="table-body__logo-text")
print(country)


# In[121]:


country = []
for i in soup.find_all('span',class_="table-body__logo-text")[0:10]:
    country.append(i.text)
    print(country)


# In[122]:


country[0]= 'PAK'
country[2]= 'IND'
print(country)


# In[123]:


rating = soup.find('td',class_="table-body__cell u-text-right rating")
print(rating)


# In[124]:


rating=[]
for i in soup.find_all('td',class_="table-body__cell u-text-right rating")[0:10]:
    rating.append(i.text)
    print(rating)


# In[125]:


rating[0]='873'
print(rating)


# In[126]:


print(len(player),len(country),len(rating))


# In[127]:


import pandas as pd


# In[128]:


df = pd.DataFrame({'player':player,'country':country,'rating':rating})
print(df)


# In[129]:


#####top 10 bowlers###


# In[162]:


soup = BeautifulSoup(bowler_page.content, "html.parser")
soup


# In[163]:


bowler_page = requests.get("https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling")
print(bowler_page)


# In[164]:


bowler1 = soup.find('div',class_="rankings-block__banner--name-large")
print(bowler1)


# In[165]:


bowler1 = []
for i in soup.find_all('div',class_="rankings-block__banner--name-large"):
    bowler1.append(i.text)
    print(bowler1)


# In[166]:


bowler2 = soup.find('td',class_="table-body__cell rankings-table__name name")
print(bowler2)


# In[167]:


bowler2 = []
for i in soup.find_all('td',class_="table-body__cell rankings-table__name name")[0:9]:
    bowler2.append(i.text)
    print(bowler2)


# In[168]:


Bowlers = bowler1 + bowler2
print(Bowlers)


# In[179]:


team =soup.find('div',class_="rankings-block__banner--nationality")
print(team)


# In[184]:


Team = []
for i in soup.find_all('span',class_="table-body__logo-text")[0:10]:
    Team.append(i.text)
    print(Team)


# In[173]:


rating1 = soup.find_all('div',class_="rankings-block__banner--rating")
print(rating1)


# In[174]:


rating1 = []
for i in soup.find_all('div',class_="rankings-block__banner--rating"):
    rating1.append(i.text)
    print(rating1)


# In[175]:


rating2 = soup.find('td',class_="table-body__cell rating")
rating2


# In[176]:


rating2 = []
for i in soup.find_all('td',class_="table-body__cell rating")[0:9]:
    rating2.append(i.text)
    print(rating2)


# In[177]:


Rating = rating1+rating2
print(Rating)


# In[185]:


print(len(Bowlers),len(Team),len(Rating))


# In[186]:


bowlers_df = pd.DataFrame({'Bowlers':Bowlers,'Team':Team,'Rating':Rating})
print(bowlers_df)


# In[ ]:




