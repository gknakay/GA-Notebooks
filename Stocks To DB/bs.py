# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 16:20:41 2022

@author: Gökhan Akay
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd

stock = 'KCHOL'

html_text = requests.get('https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/sirket-karti.aspx?hisse='+stock).text
#print(html_text)

soup = BeautifulSoup(html_text, 'lxml')
table = soup.find('tbody', id = 'tbodyMTablo')
trs = table.find_all('tr')



quarter_list = []
for i in range(0,4):
    quarter_list.append(soup.find_all('th', class_ = 'form-group')[0].find_all('option')[i].text)



val_list = []
for i in range(1,len(trs)):
    val_list.append(trs[i].find_all('td'))
    
    
col_list = []
for i in range(0,len(val_list)):
    col_list.append(val_list[i][0].text)
    
col_list[0]
col_list.remove('Gelir Tablosu')
try:
    col_list.remove('Dipnot')
except:
    pass


try:
    col_list.remove('Nakit Akım Tablosu')
except:
    pass


    
q1 = []    
for i in range(0,len(val_list)):
    try:
        q1.append(val_list[i][1].text)
    except:
        i = i+1
        
q1[0]

q2 = []    
for i in range(0,len(val_list)):
    try:
        q2.append(val_list[i][2].text)
    except:
        i = i+1

q2[0]


q3 = []    
for i in range(0,len(val_list)):
    try:
        q3.append(val_list[i][3].text)
    except:
        i = i+1

q3[0]

q4= []    
for i in range(0,len(val_list)):
    try:
        q4.append(val_list[i][4].text)
    except:
        i = i+1   
    
q4[0]

df = pd.DataFrame(index = col_list)
df['q1'] = q1
df['q2'] = q2
df['q3'] = q3
df['q4'] = q4

df.columns = quarter_list

#df.to_csv(stock+'.csv', encoding = 'utf-8-sig', sep = '\t')
df.to_excel(stock+'.xlsx')
