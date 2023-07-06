#!/usr/bin/env python
# coding: utf-8

# In[7]:


import csv
from datetime import datetime

from datetime import date
def cal_age(d):
    td=date.today() #today date
    age=td.year-d.year-((td.month,td.day)<(d.month,d.day))
    return age

f1 = open("player.csv",'r')
f2 = open("odi.csv",'r')
f3 = open("Final.csv",'w')
data1 = list(csv.reader(f1))
data2 = list(csv.reader(f2))
data3 = []

# Append all csv files into one file
for i in range(len(data1)):
    data3.append(data1[i] + data2[i])

fc = csv.writer(f3)
fc.writerows(data3)

sr=[]  #LIST
bd=[]  #LIST
city=[]  #LIST
ty=[]; type=()  #TUPLE
odiscore={}     #DICTIONARY 

for i in range (len(data1)):
    odi=[]
    sr.append(int(data1[i][0]))
    d=datetime.strptime(data1[i][2],"%d-%m-%Y") #in this line DOB is Converted into age
    bd.append(str(cal_age(d)))
    city.append(data1[i][4])
    
    ty.append((data1[i][3]))
    type = tuple(ty)
    
    odi.append(data2[i][0])
    odi.append(data2[i][1])
    odi.append(data2[i][2])
    odi.append(data2[i][3])
    odi.append(data2[i][4])
    odiscore.update({data1[i][1]:odi})

print("Serial Number = ",sr,"\n")
print("Age = ",bd,"\n")
print("City = ",city,"\n")
print("Type = ",type,"\n")
print("Dictionary = ",odiscore,"\n")    
    
    
# PLAYER WHO PLAYED MOST MATCHES IN ODI
max_matches = 0
player_name = ''
for player in odiscore.keys():
    if max_matches < int(odiscore[player][0]):
        max_matches = int(odiscore[player][0])
        player_name = player
print("Player who played the most matches in ODI:", player_name)

# PLAYER WHO SCORED MOST RUNS IN ODI
max_runs = 0
player_name = ''
for player in odiscore.keys():
    if max_runs < int(odiscore[player][1]):
        max_runs = int(odiscore[player][1])
        player_name = player
print("Player who scored the most runs in ODI:", player_name)

# PLAYER WHO TOOK MOST WICKETS IN ODI
max_wickets = 0
player_name = ''
for player in odiscore.keys():
    if max_wickets < int(odiscore[player][2]):
        max_wickets = int(odiscore[player][2])
        player_name = player
print("Player who took the most wickets in ODI:", player_name)

# Count of players who scored 0 half-century
count_0_half_centuries = 0
for player in odiscore.keys():
    if int(odiscore[player][4]) == 0:
        count_0_half_centuries += 1
print("Count of players who scored 0 half-century in ODI:", count_0_half_centuries)

# Count of players who scored 1 or more half-century
count_1_plus_half_centuries = 0
for player in odiscore.keys():
    if int(odiscore[player][4]) > 0:
        count_1_plus_half_centuries += 1
print("Count of players who scored 1 or more half-century in ODI:", count_1_plus_half_centuries)

# Count of players who scored 1 or more century
count_1_plus_centuries = 0
for player in odiscore.keys():
    if int(odiscore[player][3]) > 0:
        count_1_plus_centuries += 1
print("Count of players who scored 1 or more centuries in ODI:", count_1_plus_centuries)

# YOUNGEST PLAYER AGE
youngest_age = min(map(int, bd))
print("Youngest player age is:", youngest_age)

# OLDEST PLAYER AGE
oldest_age = max(map(int, bd))
print("Oldest player age is:", oldest_age)

# Count number of batsmen
count_batsmen = type.count("Batsman")
print("Count of batsmen in the Indian team:", count_batsmen)

# Count number of bowlers
count_bowlers = type.count("Bowler")
print("Count of bowlers in the Indian team:", count_bowlers)

# Count number of all-rounders
count_all_rounders = type.count("All-Rounder")
print("Count of all-rounders in the Indian team:", count_all_rounders)

# Count number of keepers
count_keepers = type.count("Keeper")
print("Count of keepers in the Indian team:", count_keepers)

f1.close()
f2.close()
f3.close()


# In[ ]:




