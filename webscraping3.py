import requests
import time
from bs4 import BeautifulSoup
import byebyebirdie
import json
import sqlite3


connection = sqlite3.connect('covidproject.db')
cursor = connection.cursor()

url = 'https://ncov2019.live/'
headers = {'User-Agent':'Mozilla/5.0'}
response = requests.get(url, headers = headers)
response.status_code

soup = BeautifulSoup(response.content,'html.parser')
stat_table = soup.find_all("table", attrs={"class": "display responsive"})

headers = [header.get_text(strip=True) for header in soup.find_all("th")]
rows = [dict(zip(headers, [td.get_text(strip=True) for td in row.find_all("td")]))
        for row in soup.find_all("tr")[1:-1]]
  
def update():
    cursor.execute("DROP TABLE IF EXISTS covid ")

    cursor.execute("CREATE TABLE IF NOT EXISTS covid (name STRING, confirmed REAL, changes_today REAL,deceased REAL,active REAL, recovered REAL)")

    i=9
    while 8<i<223:
        newname=rows[i]['Name']
        newname= ''.join(rows[i]['Name'].split('\u2605'))
        print (newname)
        roa=newname
        rob=rows[i]['Confirmed']
        roc=rows[i]['Changes Today']
        rod=rows[i]['Deceased']
        roe=rows[i]['Active']
        rof=rows[i]['Recovered']
        cursor.execute("INSERT INTO covid VALUES('"+newname+"','"+rob+"','"+roc+"','"+rod+"','"+roe+"','"+rof+"')")
        connection.commit()
        i=i+1

while True:
    time.sleep(60)
    update()
##print (json.dumps(rows[9], indent=2))
##print (rows[222]['Name'])

