import numpy as np
import pandas as pd

data = {"Apple": [102, 150, 175, 200, 215, 230], "Pineapple": [150, 185, 200, 220, 240, 280]}
df = pd.DataFrame(data)
df['Grapes'] = df['Apple'] - 20
df['Grapes'] = df['Apple'] - 20
df['Banana'] = df['Grapes'] - 60
df['Oranges'] = df['Grapes'] - 10
df['Strawberries'] = df['Apple'] + 30
df['Guava'] = df['Banana'] + 25
# print(df)


# head()
# print(df.head())
# print(df.head(2))

# tail()
# print(df.tail())
# print(df.tail(2))

# empty
# print(df.empty)

# values
# print(df.values)

# keys()
# print(df.keys())

# describe() statistical calculation
# print(df.describe())

# Transpose
# print(df.T)
# print(df.iloc[1])

# sum()
# print(df.sum())
# print(df.sum(0))
# print(df.sum(1))

# mean()
# print(df.mean())
# print(df.mean(1))

# median()
# print(df.median())
# print(df.median(1))

# mode()
# print(df.mode())
# print(df.mode(1))

# std()
# print(df.std())
# print(df.std(1))

# min() & max()
# print(df.min())
# print(df.min(1))
# print(df.max())
# print(df.max(1))


''' DATA CLEANING & MANIPULATION '''
data1 = np.random.rand(10, 3)
data2 = np.random.rand(7, 3)
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
# print(df1)
# print(df2)
df3 = pd.concat([df1, df2], ignore_index=True)
# print(df3)

'''
for i in df3[2]:
    print(i)

for key, values in df3.iteritems():
    print(key, values)

for row_index, row in df3.iterrows():
    print(row_index, row)

for row in df3.itertuples():
    print(row)
# '''

# sort()
# print(df3.sort_index())
# print(df3.sort_index(axis=1, ascending=False))
# print(df3.sort_values(by=2))  # according to the col-2
# print(df3.sort_values(by=0, kind='quicksort'))


# DELETE ROWS
# print(df3.drop([8, 15]))


# correlation
# print(df3[0].corr(df3[2]))
# print(df3.corr())


# reindexing
# print(df3.reindex(["a", "b", "c"]))


df = pd.DataFrame(np.random.rand(6, 6), index=["a", "c", "e", "g", "i", "k"], columns=["col1", "col2", "col3", "col4",
                                                                                       "col5", "col6"])
# print(df)
df = df.reindex(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"])
# print(df)

# isnull()
# print(df.isnull())
# print(df['col1'].isnull())
# print(df.isnull().sum())
# print(df.isnull().sum(1))
# print(df.isnull().sum().sum())
# print(df.loc['b'].isnull())

# notnull()
# print(df.notnull())
# print(df.notnull().sum())
# print(df.notnull().sum(1))
# print(df.notnull().sum().sum())
# print(df.loc['c'].notnull())

# count()  non NaN values
# print(df.count())


# methods to fill NaN values
# 1. Forward method (pad/fill)
# 2. Backward method (bfill/backfill)
# print(df.fillna(method='pad', axis=1))
# print(df.fillna(method='bfill', axis=1))


# dropna()  drops NaN values
# print(df.dropna())
# print(df.dropna(axis=1))


# replace()
'''
data = {"Apple": [102, 150, 175, 200, 215, 230], "Pineapple": [150, 185, 200, 220, 240, 280]}
df = pd.DataFrame(data)
print(df)
print(df.replace({102: 120}))
# '''

# Handling Duplicates
# check duplicates
# print(df.duplicated())
# drop duplicates
# print(df.drop_duplicates())
# print(df.drop_duplicates(subset=['col2']))


# Import/Export dataset
# data = pd.read_csv("file_path")  # data imported
# datas = df.to_csv("file_name.extension", 'location')

# print(df.info())
