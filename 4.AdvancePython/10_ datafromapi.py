import requests
import json
import pandas as pd
import csv
from requests.api import head
from openpyxl.workbook import Workbook


url='http://api.coincap.io/v2/assets'

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}
response_API = requests.request("GET",url,headers=headers,data={})
status = response_API.status_code
myjson = response_API.json()
# print(myjson)

ourdata = []
csvheader= ['ID','RANK','SYMBOL','NAME','SUPPLY','MAXSUPPLY','MARKETCAPUSD','VOLUMNUSD24HRS','PRICEUSD','CHANGEDPERCENT24HRS','VWAP24HRS','EXPLORER']

for i in myjson['data']:
    listing = [i['id'],i['rank'],i['symbol'],i['name'],i['supply'],i['maxSupply'],i['marketCapUsd'],i['volumeUsd24Hr'],i['priceUsd'],i['changePercent24Hr'],i['vwap24Hr'],i['explorer']]
    ourdata.append(listing)
# print(ourdata)
with open('crypto.csv','w',encoding='UTF8',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(csvheader)
    writer.writerows(ourdata)

read_file = pd.read_csv (r'C:\Users\pradkumar\Documents\Python\crypto.csv')
read_file.to_excel(r'C:\Users\pradkumar\Documents\Python\crypto.xlsx', index = None, header=True)


