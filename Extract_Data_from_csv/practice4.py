import pandas as pd
import numpy as np

json_string = "[{'year': '2013', 'value': '11370', 'sex': 'Both Sexes', 'reliabilty': 'Final figure, complete'}, {'year': '2012', 'value': '11304.5', 'sex': 'Both Sexes', 'reliabilty': 'Final figure, complete'}, {'year': '2011', 'value': '11226.5', 'sex': 'Both Sexes', 'reliabilty': 'Final figure, complete'}, {'year': '2010', 'value': '11156.5', 'sex': 'Both Sexes', 'reliabilty': 'Final figure, complete'}, {'year': '2009', 'value': '11064', 'sex': 'Both Sexes', 'reliabilty': 'Final figure, complete'}, {'year': '2008', 'value': '10954', 'sex': 'Both Sexes', 'reliabilty': 'Final figure, complete'}, {'year': '2007', 'value': '10863', 'sex': 'Both Sexes', 'reliabilty': 'Final figure, complete'}, {'year': '2000', 'value': '10488', 'sex': 'Both Sexes', 'reliabilty': 'Final figure, complete'}]"

df = pd.read_json(json_string)
print(df)
# df.to_csv("PolulationCount.csv")