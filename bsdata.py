import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import bs4

url = 'http://crash.net/motogp/results/981858/1/2021-dutch-motogp-assen-full-qualifying-results'
r = requests.get(url)
web_content = r.text
soup = BeautifulSoup(web_content, 'lxml')
#-----------------------------------------------------------------------------------------------------------------------

title = soup.find('div' ,class_=["table-overflow"]).tbody.find_all('tr')
#Riders-----------------------------------------------------------------------------------------------------------------
Rider = [t.find('a') for t in title]
resRider = []
resRider = list(filter(None, Rider))
resRider = str(resRider)
dr = re.compile(r'<[^>]+>',re.S)
dd = dr.sub('',resRider)
resRider = dd.split(',')
#Teams------------------------------------------------------------------------------------------------------------------
Teams = [t.find_all('td') for t in title]
data = []
Teams = str(Teams)
dr = re.compile(r'<[^>]+>',re.S)
dd = dr.sub('',Teams)
Teams = dd.split(',')
print(Teams)
#-----------------------------------------------------------------------------------------------------------------------
'''
df = pd.DataFrame(
{
    'Riders': resRider,
})
df.index=(df.index+1)
print(df)

'''

