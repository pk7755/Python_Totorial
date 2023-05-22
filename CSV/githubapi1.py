import csv
import requests
import pandas as pd


df = pd.read_csv('countryName.csv')
df["populationCounts"].apply(pd.Series)
df = pd.concat([df, df["populationCounts"].apply(pd.Series).get('year')], axis=1)
df.to_csv("PolulationCount1.csv")



