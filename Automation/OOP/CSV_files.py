import pandas as pd

names = ['age', 'workclass', 'fnlgwt']

df = pd.read_csv("adult.xlsx", header=None, names=names)

print(df.head())