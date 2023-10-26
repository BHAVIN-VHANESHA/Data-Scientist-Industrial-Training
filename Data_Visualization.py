import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as se


# plt.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the axes.
# plt.show()


x = np.random.rand(10)  # if x-axis is not given, by default it will start from 0
y = np.random.rand(10)

''' Markers
plt.plot(x, y, 'o')  # 'o' is dot marker
plt.show()
plt.plot(x, y, '*', ms=12, mec='r')  # 'ms' is marker size, 'mec' is marker edge color
# 'mfc' is marker face/body color & color code can also be selected
plt.show()
# '''

''' Lines
1. solid line(-)
2. dotted linecache(:)
3. dashes line(--)
4. dashed dotted line(-.)
'''

''' Format String(fmt) helps to draw distinct plots
# SYNTAX: marker|line|color
plt.plot(x, y, 'd:g')
plt.show()
plt.plot(x, y, 'o-k')
plt.show()
plt.plot(x, y, 'p--r')
plt.show()
plt.plot(x, y, 's-.b')
plt.show()
# '''


''' Multiple plots
plt.plot(x, 'p', ls='-.', linewidth=3, mec='r', mfc='b', markersize=20)
plt.plot(y)
plt.show()
# '''


''' Parts of Figure
plt.plot(x)
plt.plot(y)

# you can customise the label: create a dict or just pass parameters
modify = {"color": 'blue', "fontsize": 12, "family": 'serif'}
plt.xlabel('x-axis', fontdict=modify)
plt.ylabel('y-axis')

plt.title('Random Values', color='r',  fontsize=12, family='serif', loc='right')
plt.grid(color='black', ls=':', linewidth=1)
# plt.grid(axis='x')
# plt.grid(axis='y')

plt.show()
# '''


''' Subplots
# SYNTAX: plt.subplot(row,col,plot number)
# x1 = [1, 9, 2, 5, 6, 4, 8]
# y1 = [10, 7, 3, 0, 2, 9, 8]
# plt.subplot(1, 2, 1)
# plt.plot(x1, y1)
#
# plt.subplot(1, 2, 2)
# x1 = [1, 9, 2, 5, 6, 4, 8]
# y1 = [10, 7, 3, 0, 2, 9, 8]
# plt.plot(x1, y1)

plt.subplot(2, 2, 1)
plt.plot(x, y)
plt.subplot(2, 2, 2)
plt.plot(x, y)
plt.subplot(2, 2, 3)
plt.plot(x, y)
plt.subplot(2, 2, 4)
plt.plot(x, y)

plt.suptitle('random values')  # for all the plots

plt.show()
# '''


# Types of Graphs/Plots
''' 1. Scatter Plot(relation b/w two features)
# plt.scatter(x, y)

df = pd.read_csv("D:\\Data Scientist Industrial Training\\Datasets\\shopping_trends_updated.csv")
# print(df.head())

plt.scatter(df.Purchase_Amount_USD, df.Item_Purchased, color='red', s=10, alpha=0.5)
plt.show()
# '''

''' 2. Bar Plot(comparison)
x = ['one', 'two', 'three', 'four']
y = [10, 20, 15, 30]
plt.bar(x, y)
# plt.barh(x, y)
plt.show()
# '''

''' Histogram(frequency distribution)
x = np.random.normal(200, 10, 300)
plt.hist(x)
plt.show()
# '''

# ''' Pie Chart
data = np.random.rand(5)
plt.pie(data, labels=['chutiya', 'virgin', 'tharki', 'gandu', 'madarchod'], startangle=90, shadow=True,
        explode=[0.3, 0.1, 0.5, 0.4, 0.2])
plt.legend(title="log aas-pas")
plt.show()
# '''
