import requests
import pandas as pd
import csv
from requests.api import head

url='https://countriesnow.space/api/v0.1/countries/population/cities'



headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}
response_API = requests.request("GET",url,headers=headers,data={})
status = response_API.status_code
myjson = response_API.json()
# print(myjson)


ourdata = []
csvheader= ['City', 'Country','populationCounts']

for i in myjson['data']:
    listing = [i['city'],i['country'],i['populationCounts']]
    ourdata.append(listing)
# print(ourdata)
with open('countryName.csv','w',encoding='UTF8',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(csvheader)
    writer.writerows(ourdata)

df = pd.read_csv (r'C:\Users\pradkumar\Documents\Python\countryAndCityName.csv')



