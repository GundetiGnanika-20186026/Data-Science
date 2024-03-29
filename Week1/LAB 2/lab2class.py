# -*- coding: utf-8 -*-
"""Lab2class.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lFEcmOctTdZrejKeVrGJR4tdWtNW662o
"""

import requests

req = requests.get("https://en.wikipedia.org/wiki/Harvard_University")

req

type(req)

dir(req)

page = req.text

page

from bs4 import BeautifulSoup

soup = BeautifulSoup(page, 'html.parser')
soup

type(page)

type(soup)

print (soup.prettify())

soup.title

"title" in dir(soup)

soup.p

len(soup.find_all("p"))

soup.table["class"]

[t["class"] for t in soup.find_all("table") if t.get("class")]

my_list = []
for t in soup.find_all("table"):
    if t.get("class"):
        my_list.append(t["class"])
my_list

table_html = str(soup.findAll("table", "wikitable")[2])

from IPython.core.display import HTML

HTML(table_html)

rows = [row for row in soup.find_all("table", "wikitable")[2].find_all("tr")]
rows

rem_nl = lambda s: s.replace("\n", "")

##### FUNCTIONS

def power(x, y):
    return x**y

power(2, 3)

def product(a,b):
    return a*b;
product(10,5)

def printName():
    return "name"
print(printName())

def print_greeting():
    print ("Hello!")
    
print_greeting()

def get_multiple(x, y=1):
    return x*y

print ("With x and y: ", get_multiple(10, 2))
print ("With x only: ", get_multiple(10))

def printAll(name, *listV):
    print(name, "has the following values:")
    for i in listV:
        print(i)
    print
        
printAll("List", 1, 2, 3)
printAll("List", 1)
printAll("List")

def print_special_greeting(name, leaving=False, condition="nice"):
    print ("Hi", name)
    print ("How are you doing in this", condition, "day?")
    if leaving:
        print ("Please come back!")
        
print_special_greeting("John")

print_special_greeting("John", True, "rainy")

print_special_greeting("John", True)

print_special_greeting("John", condition="horrible")

def print_siblings(name, *siblings):
    print (name, "has the following siblings:")
    for sibling in siblings:
        print( sibling)
    
        
print_siblings("John", "Ashley", "Lauren", "Arthur")
print_siblings("Mike", "John")
print_siblings("Terry")

def print_brothers_sisters(name, **siblings):
    print(name, "has the following siblings:")
    for sibling in siblings:
        print (sibling, ":", siblings[sibling])
    print()
    
print_brothers_sisters("John", Ashley="sister", Lauren="sister", Arthur="brother")

columns = [rem_nl(col.get_text()) for col in rows[0].find_all("th") if col.get_text()]
columns

HTML(table_html)

to_num = lambda s: s[-1] == "%" and int(s[:-1]) or None

values = [to_num(rem_nl(value.get_text())) for row in rows[1:] for value in row.find_all("td")]

values

stacked_values = zip(*[values[i::3] for i in range(len(columns))])
list(stacked_values)

indexes = [rem_nl(row.find("th").get_text()) for row in rows[1:]]
indexes

HTML(table_html)

def exampleParameter(a,b,c):
    print(a,b,c)
exampleParameter(1,2,3)
exampleParameter([1,2], [3,4], [5,6])

params = [1,2,3]
a = params[0]
b = params[1]
c = params[2]
exampleParameter(a,b,c)

a1, b1, c1 = params
exampleParameter(a1,b1,c1)

exampleParameter(*params)

import pandas as panda

stacked_values = zip(*[values[i::3] for i in range(len(columns))])
pText = panda.DataFrame(stacked_values, columns=columns, index=indexes)
pText

columns = [rem_nl(col.get_text()) for col in rows[0].find_all("th") if col.get_text()]
stacked_values = zip(*[values[i::3] for i in range(len(columns))])
data_dicts = [{col: val for col, val in zip(columns, col_values)} for col_values in stacked_values]
data_dicts

panda.DataFrame(data_dicts, index=indexes)

stacked_colValues = [values[i::3] for i in range(len(columns))]
stacked_colValues

data_lists = {col: val for col, val in zip(columns, stacked_colValues)}
data_lists

panda.DataFrame(data_lists, index=indexes)

pText.dtypes

pText.dropna()

pText.dropna(axis=1)

pTextOpti = pText.fillna(0).astype(int)
pTextOpti

pTextOpti.dtypes

pTextOpti.describe()

########## Numpy

import numpy as nump

pTextOpti.values

type(pTextOpti.values)

nump.mean(pTextOpti.Undergrad)

nump.std(pTextOpti)

pTextOpti["Undergrad"]

pTextOpti.Undergrad

pTextOpti.loc["Asian/Pacific Islander"]

pTextOpti.iloc[0]

pTextOpti.ix["Asian/Pacific Islander"]

pTextOpti.ix[0]

pTextOpti.loc["White/non-Hispanic", "Graduate"]

pTextOpti.ix[3, "Graduate"]

pTextOpti.loc[3, 1]

sequenceTable = pTextOpti.stack().reset_index()
sequenceTable.columns = ["race", "source", "percentage"]
sequenceTable

groupedData = sequenceTable.groupby("race")
groupedData.groups

type(groupedData)

meanTable = groupedData.mean()
meanTable

type(meanTable)

for name, group in sequenceTable.groupby("source", sort=True):
    print(name)
    print(group)

########### Plottings

meanTable.plot(kind="bar");