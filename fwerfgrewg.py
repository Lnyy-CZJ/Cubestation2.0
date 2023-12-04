import pandas as pd
import openpyxl

df =pd.read_excel("../tdata.xlsx",engine='openpyxl')

df['第一单元排名'] = df['第一单元'].rank(ascending=False, method='min')
df['第二单元排名'] = df['第二单元'].rank(ascending=False, method='min')
df['进退'] = df['第一单元排名'] - df['第二单元排名']

print(df)
df.to_excel('out.xlsx', sheet_name='结果')
