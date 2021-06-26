import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import bs4

url = 'https://www.motogp.com/en/Results+Statistics/2021/NED/MotoGP/Q2'
r = requests.get(url)
web_content = r.text
soup = BeautifulSoup(web_content, 'lxml')
'''------------------------------------------------------------------------------------------------------------------'''
Etable = soup.find('table').tbody.find_all('tr')
Ntable = soup.find_all('table')
Ntable = str(Ntable)
dr = re.compile(r'<[^>]+>',re.S)
dd = dr.sub('',Ntable)
print(dd)
'''Riders------------------------------------------------------------------------------------------------------------'''
Eriders = []
for row in Etable:
    rid = row.find_all('td')[2].text
    Eriders.append(rid)
'''Teams-------------------------------------------------------------------------------------------------------------'''
ETeam = []
for row in Etable:
    tea = row.find_all('td')[4].text
    ETeam.append(tea)
'''Kmh---------------------------------------------------------------------------------------------------------------'''
EKmh = []
for row in Etable:
    km = row.find_all('td')[6].text
    EKmh.append(km)
'''Time--------------------------------------------------------------------------------------------------------------'''
ETime = []
for row in Etable:
    tm = row.find_all('td')[7].text
    ETime.append(tm)
'''------------------------------------------------------------------------------------------------------------------'''
df = pd.DataFrame(
{
    'Riders': Eriders,
    'Teams': ETeam,
    'Kmh':EKmh,
    'Fast Lap':ETime
})
df.index=(df.index+1)*2
print(df)

'''
for i in range(1, len(title)):
    riderData = title[i].find_all("td" ,class_=["alignright"])
    print(riderData)

'''