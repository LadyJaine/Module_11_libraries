#https://httpbin.org/
#https://smartiqa.ru/blog/python-requests
import requests
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

# https://blog.skillfactory.ru/kak-nachat-analizirovat-dannye-v-pandas-pervye-shagi/
# https://blog.skillfactory.ru/chto-takoe-google-colaboratory-i-komu-on-nuzhen/
# https://blog.skillfactory.ru/chto-takoe-google-colaboratory-i-komu-on-nuzhen/
# https://smysl.io/blog/pandas/#%D0%A7%D1%82%D0%BE-%D1%82%D0%B0%D0%BA%D0%BE%D0%B5-Pandas-%D0%B8-%D0%B7%D0%B0%D1%87%D0%B5%
# D0%BC-%D0%BE%D0%BD-%D0%BD%D1%83%D0%B6%D0%B5%D0%BD
import numpy as np
import pandas as pd
import openpyxl
df = pd.read_csv('post2.csv', sep='\t')
print(df)
print()
print(f'первые 6 строк {df.head()}')
print()
print(f"размер таблицы {df.shape}")     #покажет размеры сразу по двум осям df.shape[0]
print()
print(f"количество строк {df.shape[0]}") #размер по горизонтали - то есть количество строк
print(f"количество столбцов {df.shape[1]}")  #размер по горизонтали - то есть количество столбцов
print()
print(df.columns)

df1 = pd.read_excel('post_126520.xls')
print(df1)
print()
print(f'первые 6 строк {df1.head()}')
print()
print(f"размер таблицы {df1.shape}")     #покажет размеры сразу по двум осям df.shape[0] #размер по горизонтали - то есть количество строк
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