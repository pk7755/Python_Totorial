# Using Pandas to Convert a JSON String to a CSV File
import pandas as pd

json_string = '[{"Name": "Nik", "Age": 30, "Active": true}, {"Name": "Kate", "Age": 32, "Active": true}, {"Name": "Evan", "Age": 45, "Active": false}, {"Name": "Kyra", "Age": 43, "Active": true}]'

df = pd.read_json(json_string)
df.to_csv('file.csv')
df.to_excel('file.xlsx')