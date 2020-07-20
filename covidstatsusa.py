import requests
import time
from bs4 import BeautifulSoup
import json
import sqlite3

connection = sqlite3.connect('covidproject.db')
cursor = connection.cursor()

url = 'https://ncov2019.live/'
headers = {'User-Agent':'Mozilla/5.0'}
response = requests.get(url, headers = headers)
response.status_code

soup = BeautifulSoup(response.content,'html.parser')
stat_table = soup.find_all("table", attrs={"class": "display responsive dataTable no-footer"})

headers = [header.get_text(strip=True) for header in soup.find_all("th")]
lines = [dict(zip(headers, [td.get_text(strip=True) for td in line.find_all("td")]))
        for line in soup.find_all("tr")[1:-1]]
##print (lines[299]['Name'])
##print (lines[287]['Name'])

i=225
print (lines[224])
print (lines[287])
def inserttt():
    while 224<i<286:
        new_name=lines[i]['Name']
        new_name= ''.join(lines[i]['Name'].split('\u2605'))
        print (new_name)
        lia=new_name
        lib=lines[i]['Confirmed']
        lic=lines[i]['Changes Today']
        lid=lines[i]['Deceased']
        lie=lines[i]['Active']
        lif=lines[i]['Recovered']
        cursor.execute("INSERT INTO covidusa VALUES('"+new_name+"','"+lib+"','"+lic+"','"+lid+"','"+lie+"','"+lif+"')")
        connection.commit()
        i=i+1

while True:
    time.sleep(300)
    cursor.execute("DROP TABLE IF EXISTS covidusa ")
    cursor.execute("CREATE TABLE IF NOT EXISTS covidusa (name STRING, confirmed REAL, changes_today REAL,deceased REAL,active REAL, recovered REAL)")
    inserttt()
##print (json.dumps(lines, indent=2))
##
##print(lines)
