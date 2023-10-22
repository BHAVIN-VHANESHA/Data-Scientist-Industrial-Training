""" Most imp data structure in PANDAS is DataFrame
SYNTAX:- pd.DataFrame(data, index, column, dtype, copy)
"""
import pandas as pd

# C R E A T E
''' different methods to create dataframe (list, dict, ndarrays, series) '''
'''empty dataframe
df = pd.DataFrame()
print(df)
# '''


''' Series
df = pd.Series([1, 2, 3, 4, 5, 6, ["dog", "bhaw bhaw"], ["cat", "meow"], ["cow", "moo"]])
print(df)
data = [["dog", "bhaw bhaw"], ["cat", "meow"], ["cow", "moo"]]
df = pd.DataFrame(data, columns=["animal_name", "animal_sound"])
print(df)
data = {"s-1marks": pd.Series([55, 87, 67], index=["test1", "test2", "test3"]),
        "s2-marks": pd.Series([63, 60, 78], index=["test", "test2", "test4"])}
df = pd.DataFrame(data, columns=["a", "b"   ])
print(df)
# '''


''' List
data = [1, 2, 3, 4, 5, 6]
df = pd.DataFrame(data)
print(df)
data = [{"a": "@", "b": "#"}, {'c': '!', 'd': '$'}, {"E": "%", "F": "^"}]
df = pd.DataFrame(data, index=["->", "->", "->"], columns=["1", "2", "3", "4", "5", "6"])
print(df)
# '''


''' Dict
data = {"Name": ["bhavin", "kevin", "ram", "sita", "radha", "kanha"], "Age": ["20", "23", "25", "24", "19", "22"]}
df = pd.DataFrame(data, index=["a", "b", "c", "d", "e", "f"])
print(df)
# '''


# U P D A T E
data1 = [10, 20, 30, 40, 50, 60, 70]
data2 = [100, 200, 300, 400, 500, 600, 700]
df = pd.DataFrame([data1, data2], columns=["a", "b", "c", "d", "e", "f", "g"])
# print(df)

'''col selection
print(df["a"])
# print(df["h"])
df["h"] = 90
print(df["h"])
# '''


# D E L E T E
del df['a']
print(df)

# pop()
df.pop('g')
print(df)

print(df[['b', 'c']])
print(df.drop(['d', 'e'], axis=1))  # col = axis1
print(df)
