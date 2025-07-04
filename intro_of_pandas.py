# -*- coding: utf-8 -*-
"""Intro of pandas.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1DKgF9XSgvRJikQj_KzOyR0Ruilrk63a7

# Create Dataframe
## From array
"""

import numpy as np
import pandas as pd

# create array
data = np.array([[1, 4], [2, 5], [3, 6]])
df = pd.DataFrame(data, index = ["r1", "r2", "r3"],
                  columns = ["c1", "c2"])
df

dt = [[1, 4], [2, 5], [3, 6]]
df = pd.DataFrame(dt, index = ["r1", "r2", "r3"],
                  columns = ["c1", "c2"])
df

"""## From dictionary"""

state = ["California", "Texas", "Washington", "New York"]
population = [4534893, 2589103, 8359204, 20505820]

# store list in the dictionary
dictionary = {'States' : state, 'Population' : population}

df_population = pd.DataFrame(dictionary)
df_population

# import file from computer
from google.colab import files
uploaded = files.upload()
df = pd.read_csv('ad_data.csv')
df

# import data from google drive
from google.colab import drive
drive.mount('/content/drive')
file_path = '/content/drive/MyDrive/Colab Notebooks/data.csv'
df = pd.read_csv(file_path)
df

# import data from github
url = 'https://raw.githubusercontent.com/Jovinahu/Jovinahu/main/AS-N100.tsv'
df = pd.read_csv(url, sep = '\t')
df

df.head()

df.tail()

df.shape

"""# Select Columns
## data
"""

import pandas as pd

# data
url = 'https://raw.githubusercontent.com/Jovinahu/Jovinahu/main/AS-N100.tsv'
data = pd.read_csv(url, sep = '\t')
data.head()

"""## Select one column"""

# using []
data['ticker']

# data type of the selected column
type(data['ticker'])

data['ticker'].index
data['ticker'].head()

# using .
data.ticker

"""## Select two or more cols"""

# using [[]]
data[['ticker', 'open']]

type(data[['ticker', 'open']])

# select more than 2 cols
data[['ticker', 'open', 'close', 'high', 'low', 'close']]

"""# Adding New Column
## Data
"""

import pandas as pd

url = 'https://raw.githubusercontent.com/Jovinahu/Jovinahu/main/AS-N100.tsv'
data = pd.read_csv(url, sep = '\t')
data.head()

"""## Adding with a scaler value"""

data['total'] = 100
data.head()

"""## Adding with an array"""

import numpy as np

# create an array of 10000 elements
total = np.arange(0, 10000)
len(total)

# add a new column to the data
data['total'] = total
data

# create random integers from 1 to 500
int_total = np.random.randint(1, 500, size = 10000)
print(max(int_total))
print(min(int_total))

data['total'] = int_total
data

# create random float numbers btw 1 to 500
np.random.uniform(1, 500, size = 10000)

"""## Using assing()

- when adding multiple columns in a single line of code
- when you need to overwrite values in an existing columns

  => returns a new object with original columns in addition to the new ones
"""

import numpy as np
import pandas as pd

url = 'https://raw.githubusercontent.com/Jovinahu/Jovinahu/main/AS-N100.tsv'
data = pd.read_csv(url, sep = '\t')
data.head()

trade_in = np.random.randint(1, 1000, size = 10000)
trade_out = np.random.randint(1, 1000, size = 10000)

serie1 = pd.Series(trade_in, index = np.arange(0, 10000))
serie2 = pd.Series(trade_out, index = np.arange(0, 10000))

df = data.assign(trade_in = serie1, trade_out = serie2)
df

"""## Using insert()
      
  insert a new column at a specific position / index
"""

# insert a column at index 2
df.insert(2, 'test', serie1)
df

"""# Math Operation

## Data
"""

import pandas as pd

url = 'https://raw.githubusercontent.com/Jovinahu/Jovinahu/main/AS-N100.tsv'
data = pd.read_csv(url, sep = '\t')
data.head()

"""## operation in columns"""

data['quantity'].sum()

data['quantity'].count()
data['quantity'].mean()
data['quantity'].min()
data['quantity'].max()
data['quantity'].std()

# easier calculation with describe
data.describe()

"""## operation in rows"""

data['open'] + data['high'] + data['low']

# calculate the average and assign the result to the new col
data['average'] = (data['high'] - data['low']) / 2
data

"""## Value Counts"""

# counting the tickers elements

len(data['ticker'])

data['ticker'].count()

# count tickers by category
data['ticker'].value_counts()

# return the relative frequency
data['ticker'].value_counts(normalize = True)

data['tradecount'].value_counts()

# round it to 2 decimals
data['tradecount'].value_counts(normalize = True).round(2)

"""## Sort the dataframe"""

# sort by one column
data.sort_values('tradecount')

# sort in descending order by one column
data.sort_values('tradecount', ascending = False)

# sort multiple columns
data.sort_values(['quantity', 'volume'], ascending = False)

# sort by multuple cols and update the dataframe
data.sort_values(['quantity', 'volume'], ascending = False, inplace = True)

# sort descending with key function
data.sort_values(['ticker'], ascending = True, key = lambda a:a.str.lower())

"""## Create index"""

import pandas as pd
import numpy as np
import random

url = 'https://raw.githubusercontent.com/Jovinahu/Jovinahu/main/AS-N100.tsv'
data = pd.read_csv(url, sep = '\t')

# create non-repetitive values for the index
new_index = np.arange(0, 10000)
new_index

# shuffling the index
random.shuffle(new_index)
new_index

data['new_index'] = new_index
data.head()

"""## Set index"""

# set new index column as index
data.set_index('new_index', inplace = True)
data

"""##Sort index"""

data.sort_index()
data

# sort descending order
data.sort_index(ascending = False)
data

"""## Rename column"""

# rename column & overwrite values
data = data.rename(columns = {'ticker':'Company'})

# add the inplace parameter
data.rename(columns = {'tradecount' : 'TC', 'quantity' : 'QU'}, inplace = True)
data

"""## Rename index"""

url = 'https://raw.githubusercontent.com/Jovinahu/Jovinahu/main/AS-N100.tsv'
data = pd.read_csv(url, sep = '\t')

data.rename(index = {0:'A', 1:'B', 2:'C'}, inplace = True)
data.head(3)