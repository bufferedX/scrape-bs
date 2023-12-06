# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 22:58:54 2021

@author: basus
"""

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

def getSoup(requestUrl):
    r = requests.get(requestUrl)
    soup = bs(r.content,"lxml")
    return soup

def calcColspan(squadStat,text,colspan):
    if squadStat == "standard":
        return int(colspan)
    elif squadStat == "keeper":
      return int(colspan)
    else:
        return int(colspan)

def getTable(squadStat,mainSoup,idDict):
    soup = mainSoup.find("table" , attrs={"id":idDict[squadStat]})
    
    columnList = []
    parentColumnDict = {}
    itr = 0
    for value in soup.select("tr th[colspan]"):
        parentColumnDict[str.replace(value.text,' ','')+'_'+str(itr)] = calcColspan(squadStat,
                                                                                    value.text,
                                                                                    value.get('colspan'))
        itr+=1
    print(parentColumnDict)
    
    for child in soup.find_all("tr")[1]:
        for th in child:
            if th != ' ':
                columnList.append(th)
    print(columnList)
    
    
    iterCount = 0
    for key in parentColumnDict:
        for i in range(iterCount,iterCount+parentColumnDict[key]):
            columnList[i] = key+"_"+columnList[i]
        iterCount += parentColumnDict[key]
    print(columnList)
        
    data = []
    for i in range(0,len(soup.find("tbody").find_all('tr'))):
        temp = []
        for child in soup.find("tbody").find_all('tr')[i].children:
                temp.append(child.text)
        data.append(temp)
            
    #print(data)
    df = pd.DataFrame(data,columns=columnList)
    return df

teamIdDict = {"standard" : "stats_squads_standard_for" , "keeper" : "stats_squads_keeper_for",
          "shooting" : "stats_squads_shooting_for" , "passing" : "stats_squads_passing_for" ,
          "possession" : "stats_squads_possession_for" , "gca" : "stats_squads_gca_for",
          "defense" : "stats_squads_defense_for"}
playerIdDict = {"standard" : "stats_standard_10728" , "keeper" : "stats_keeper_10728",
          "shooting" : "stats_shooting_10728" , "passing" : "stats_passing_10728" ,
          "possession" : "stats_possession_10728" , "gca" : "stats_gca_10728",
          "defense" : "stats_defense_10728"}
teamSoup = getSoup('https://fbref.com/en/comps/9/Premier-League-Stats')
playerSoup = getSoup('https://fbref.com/en/comps/9/Premier-League-Stats#all_stats_shooting')

################################################################################

#### REVISIT LATER - DYNAMIC WEB SCRAPING (TO DO)

#print(teamSoup.find("div" , attrs={"id" : "stats_squads_standard_for_sh"}).find("a").get("href"))
#dummysoup = getSoup('https://fbref.com/'+teamSoup.find("div" , attrs={"id" : "stats_squads_shooting_for_sh"}).find("a").get("href"))
# print(dummysoup)
#print('https://fbref.com/'+teamSoup.find("div" , attrs={"id" : "stats_squads_shooting_for_sh"}).find("a").get("href"))
#print(dummysoup.find_all("table")[2])
#print(dummysoup.find("table" , attrs={"id":playerIdDict["standard"]}))

#################################################################################

def pl_all(stat):
    return getTable(stat, teamSoup, teamIdDict)

# teamList=[]
# teamDict={}
# for teamLinks in teamSoup.find("table" , attrs={"id":teamIdDict["standard"]}).find_all('a'):
#     teamDict[teamLinks.string] = 'https://fbref.com'+teamLinks.get('href')
#print(teamDict)

#pl_player_passing = pd.DataFrame()
#for temp in teamDict:
#    print('Collecting data for '+temp+' .....')
#    dummy = getTable("passing",getSoup(teamDict[temp]),playerIdDict)
#    dummy['Team'] = temp
#    pl_player_passing = pl_player_passing.append(dummy)
