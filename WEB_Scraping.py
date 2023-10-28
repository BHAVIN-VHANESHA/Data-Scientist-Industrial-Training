import pandas as pd
from bs4 import BeautifulSoup
import requests
import re

url = "https://en.wikipedia.org/wiki/List_of_Academy_Award-winning_films"
req = requests.get(url)
print(req)

# gathering datas
soup = BeautifulSoup(req.content, features="html.parser")
soup.prettify()
# print(soup)

# for i in soup:
#     print(i)


# Data Extracting
'''
arr = []
for i in soup.findAll('td'):
    # print(i)
    # storing in list
    arr.append(str(i))
# print(arr)
# print(arr[0])

print(re.sub('^<td>.*">|<td>|</td>|<.*.>', "", arr[15]))
# '''

# Extracting all datas and Manipulating
Film = []
Year = []
Awards = []
Nominations = []
count = 0

for i in soup.findAll('td'):
    i = re.sub('^<td>.*">|<td>|</td>|<.*.>|\n', "", str(i))
    if count == 0:
        Film.append(i)
        count += 1
    elif count == 1:
        Year.append(i)
        count += 1
    elif count == 2:
        Awards.append(i)
        count += 1
    elif count == 3:
        Nominations.append(i)
        count = 0
# print(f"Film Name:\n{Film}")
# print(f"Year:\n{Year}")
# print(f"Awards:\n{Awards}")
# print(f"Nominations:\n{Nominations}")
# the above code can be minimized by list comprehension


# Data Exploration
# print(len(Film))
# print(len(Year))
# print(len(Awards))
# print(len(Nominations))
# print(Awards[-3])
# print(Awards[1359])
oscar = pd.DataFrame({"Films": Film[:1360], "Years": Year[:1360],
                      "Awards": Awards[:1360], "Nominations": Nominations[:1360]},
                     columns=["Films", "Years", "Awards", "Nominations"])
# print(oscar)
print(oscar.info())
