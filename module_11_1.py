import requests
import numpy as np
import pandas as pd
import openpyxl
mesto = 'https://mail.ru/'
request_1 = requests.get(mesto)
print(request_1)
inbox = requests.get('https://e.mail.ru/inbox/')
receipts = requests.get('https://e.mail.ru/receipts/')
data = requests.get(mesto, params = {'inbox':inbox, 'receipts':receipts})
print(data)
print(data.url)
print(inbox.url)
print(inbox.text)
response = requests.options('https://mail.ru/')
print(response)
print(request_1.headers)

df = pd.read_csv('post2.csv', sep='\t')
print(df)
print()
print(f'первые 6 строк {df.head()}')
print()
print(f"размер таблицы {df.shape}")          #покажет размеры сразу по двум осям df.shape[0]
print()
print(f"количество строк {df.shape[0]}")     #размер по горизонтали - то есть количество строк
print(f"количество столбцов {df.shape[1]}")  #размер по горизонтали - то есть количество столбцов
print()
print(df.columns)

df1 = pd.read_excel('post_126520.xls')
print(df1)
print()
print(f'первые 6 строк {df1.head()}')
print()
print(f"размер таблицы {df1.shape}")          #покажет размеры сразу по двум осям df.shape[0] 
print()
print(f"количество столбцов {df1.shape[1]}")  #размер по горизонтали - то есть количество столбцов
print()
print(df1.columns)
print(df1.dtypes)
print(df1['Date'])
print()
show_these_dates = [2,5,10]
print(df1.loc[show_these_dates])
print(df1.describe())
my_df = pd.DataFrame({'id': [1, 2, 3], 'name': ['Bob', 'Alice', 'Scott'], 'age': [21, 15, 30]})
print(my_df)
print(my_df.shape)
print(my_df.shape[0])
print(my_df.shape[1])
