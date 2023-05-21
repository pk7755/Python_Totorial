import requests
import json
import pandas as pd
import csv
from requests.api import head
from openpyxl.workbook import Workbook

url='https://api.covid19india.org/state_district_wise.json'



headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}
response_API = requests.request("GET",url,headers=headers,data={})
status = response_API.status_code
myjson = response_API.json()
print(myjson)

ourdata = []
csvheader= ['Comman Name','Official Name','NativeName']

for i in myjson['JSON']:
    listing = [i['comman'],i['official'],i['nativeName']]
    ourdata.append(listing)
print(ourdata)
# with open('countryName.csv','w',encoding='UTF8',newline='') as f:
#     writer = csv.writer(f)
#     writer.writerow(csvheader)
#     writer.writerows(ourdata)

# read_file = pd.read_csv (r'C:\Users\pradkumar\Documents\Python\countryName.csv')
# read_file.to_excel(r'C:\Users\pradkumar\Documents\Python\countryName.xlsx', index = None, header=True)


