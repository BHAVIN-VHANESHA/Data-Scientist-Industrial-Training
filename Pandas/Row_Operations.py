import pandas as pd

data = {"Apple": [102, 150, 175, 200], "Pineapple": [150, 185, 200, 220]}
df = pd.DataFrame(data)
# prinmt(df)
# print(df[['Apple']])
# print(df[['Pineapple']])

df['Grapes'] = df['Apple'] - 20
# print(df)
df.drop(['Grapes'], axis=1, inplace=True)
# print(df)
df['Grapes'] = df['Apple'] - 20
df['Banana'] = df['Grapes'] - 60
df['Oranges'] = df['Grapes'] - 10
df['Strawberries'] = df['Apple'] + 30
df['Guava'] = df['Banana'] + 25
# print(df)


# Row selection
''' loc(index name) & iloc(index number)
print(df.loc[[3]])
print(df.loc[1:3])
print(df.iloc[[3]])
print(df.iloc[1:3])
# '''


# ''' concat() & append()
data1 = {"Name": ["bhavin", "kevin"], "DSA": ["100", "95"], "OS": ["87", "96"]}
df = pd.DataFrame(data1)
# print(df)
data2 = {"Name": "sita", "DSA": 90, "OS": 88}
df = df._append(data2, ignore_index=True)
# print(df)
data3 = {"Name": "ram", "DSA": 96, "OS": 89}
df3 = pd.DataFrame(data3, index=[0])
df = pd.concat([df, df3])
# print(df)
# print(df.loc[[0]])
# print(df.iloc[[0]])
# print(df.loc[2])
df.iloc[1] = ["radha", 93, 78]
# print(df)
# '''


# D E L E T E
df.drop(0, inplace=True)
# print(df)
