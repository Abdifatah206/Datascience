# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 23:30:27 2019

@author: Shire
"""
import pandas as pd


"""
data = {
    'apples': [3, 2, 0, 1], 
    'oranges': [0, 3, 7, 2]
}
purchase = pd.DataFrame(data, index = ['Abdi', 'casha', 'jama', 'ali'])
print(purchase.loc['Abdi'])
"""


#cvs file read from outside
"""
df = pd.read_csv('Salary_Data.csv')

print(df.loc[0])
"""

#json file read from outside
"""
df = pd.read_json('purchases.json')

print(df)

"""
df = pd.read_csv('Salary_Data.csv')

#prints first column you can add index of which when you want to printout
#print(df.head())

#prints last column you can add index of which when you want to printout
#print(df.tail())

#prints out information about your data
#print(df.info())

#prints out number of rows and columns
#print(df.shape)

#create duplicate
temp_df = df.append(df)
print(temp_df.shape)
#drop duplicate
temp_df = temp_df.drop_duplicates()
print(temp_df.shape)