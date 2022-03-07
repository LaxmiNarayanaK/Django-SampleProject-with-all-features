import requests
from bs4 import BeautifulSoup
import pandas as pd
# from scrap.models import BsModel

URL = "https://hdoa.hawaii.gov/hemp/licensees-by-county/"

c = requests.get(URL)

soup=BeautifulSoup(c.content,'html.parser')

d=[]
data=[[],[],[],[]]
table = soup.find('table',attrs={"border": '1',"style":"border-collapse: collapse; width: 91.1805%; height: 1318px;"})
table1 = soup.find('table',attrs={"border": '1',"style":"border-collapse: collapse; width: 91.1805%; height: 415px;"})
table.append(table1)

for j in table.find_all('td'):
        d.append(j.text)
d=d[4:]
for k in range(4):
    data[k]=d[k::4]

df = pd.DataFrame({'DateLicensed': data[0],'Name': data[1],'Island': data[2],"Contact":data[3]})

print(df)
df.to_csv("E:\Zigram\Training\Django-Files\Data\\HempLicensee.csv")

from globalfuns.Dumpdata import dump

dump(df,table="scrap_bsmodel")



# df_records = df.to_dict('records')
# print(df_records)
# for item in df_records:
#     # key=list(item.keys())
    
#     DateLicensed =  item['DateLicensed']
#     Name =  item['Name']
#     Island =  item['Island']
#     Contact =  item['Contact']
    
#     bs = BsModel(DateLicensed=DateLicensed,Name=Name,Island=Island,Contact=Contact)
#     bs.save()

