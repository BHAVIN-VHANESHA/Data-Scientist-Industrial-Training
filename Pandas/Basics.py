"""
Panel Datas(pandas)
it is the library used while working with the datasets
uses of pandas:- analyze data, clean data, explore data, manipulate data
* WHY pandas?
- allows to analyze big data
- clean messy datasets and make it readable


NOTE:- in pandas row values can be accessed by index values &
columns can be accessed by column name
"""


import pandas as pd
import numpy as np


''' Basic DataStructures in Pandas
1. Series:- a one-dimensional labeled array holding data of any type such as integers, strings, Python objects etc.
2. DataFrame:- a two-dimensional data structure that holds data like a two-dimension array or a table with rows and columns.
3. Panel:- a three-dimensional data structure that holds data like a three-dimension array or a table with rows and columns.
these data structures are built on Numpy array
'''

''' CREATE '''
# 1. Series
# it can be created using Array, Dictionary, Scalar Values
empty_series = pd.Series()
# print(empty_series)

''' Array
data = np.array([1, 2, 3, 4, 5, 6])
se = pd.Series(data, index=[1, 2, 3, 4, 5, 6])
print(se)
# '''

''' Dictionary 
data = {"A": 10, "B": 20, "C": 30, "D": 40}
se = pd.Series(data)
# here key will be index values
print(se)
se = pd.Series(data, index=["E", "F", "G", "H"])
#  the values will remain with it's assigned key
print(se)
se = pd.Series(data, index=["A", "F", "C", "B"])
print(se)
# '''

''' Scalar values
data = 96
se = pd.Series(data)
print(se)
se = pd.Series(data, index=[1, 2, 3, 4, 5, 6])
print(se)
# '''


''' UPDATE '''
# Accessing data from Series
data = np.array([20, 1, 2, 15, 11, 5, 458, 48, 46, 58])
se = pd.Series(data)
# print(se)

''' Indexing & Slicing
print(f"value at index {6} is: {se[6]}")

se[5] = 10
# value updated
print(se)

# first 3 values
print("sliced:")
print(se[:3])
# last 3 values
print("sliced:")
print(se[7:])

data = {"A": 10, "B": 20, "C": 30, "D": 40}
se = pd.Series(data, index=["C", "D", "E", "B", "A"])
# in dictionary while slicing the end pont is also inclusive
print(se["D":"B"])

# specific index values
print(se[["C", "B"]])

se["E"] = 96
print(se)
# '''


''' Boolean Masking '''
# return boolean values
# print(se < 30)
# returns the values
# print(se[se < 30])
# multiple condition
# data = (se[se] > 50) & (se[se] == 10)
# print(se[data])
# '''


''' DELETE '''
# temp delete
# print(se.drop(6))
# print(se)
# to delete permanent
# se.drop(6, inplace=True)
# print(se)
# multi delete
# print(se.drop([0, 1]))
