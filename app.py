import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import bs4

url = 'https://datamotogp.azurewebsites.net/GpResults/Index/119'
r = requests.get(url)
web_content = r.text
soup = BeautifulSoup(web_content, 'lxml')

title = soup.find('div' ,class_=["col-md-8"]).tbody.find_all('tr')
Rider = [t.find('a').text for t in title]

lapData = []
for row in title:
        rid = row.find_all('td')[5].text
        rid = float(rid)
        min = str(int(rid/60.0))
        sec = str(int(rid-60.0))
        rid = min+'.'+sec
        lapData.append(rid)
print('ITA - Race')
df = pd.DataFrame(
{
    'Riders': Rider,
    'Best5' : lapData
})
df.index=df.index+1

print(df)
