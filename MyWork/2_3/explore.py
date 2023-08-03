# doing the exercise in a python file instead of the python interactive shell

import csv
f = open('../../Data/portfolio.csv')
f_csv = csv.reader(f)
headers = next(f_csv)

print(headers)

rows = list(f_csv)
from pprint import pprint as pp
pp(rows)

# basic iter and unpacking

for row in rows:
    print(row)
    
for name, shares, price in rows:
    print(name, shares, price)

for name, shares, _ in rows:
    print(name, shares)

from collections import defaultdict
byname = defaultdict(list)
for name, *data in rows:
    byname[name].append(data)
pp(byname)

for shares, price in byname['IBM']:
    print(shares, price)
    
# counting with enumerate
for i, row in enumerate(rows):
    print(i, row)

for i, (name, shares, price) in enumerate(rows):
    print(i, name, shares, price)
    

# using the zip function
print(headers)
print(list((dict(zip(headers, row)) for row in rows)))

# generator expressions

nums = range(1, 6)
squares = (x*x for x in nums)
print(squares)
print(list(squares))
# generator used up, now empty
print(list(squares))

# generator expressions and reduction functions

from readport import read_portfolio
portfolio = read_portfolio('../../Data/portfolio.csv')
print(sum(s['shares'] * s['price'] for s in portfolio))
print(min(s['shares'] * s['price'] for s in portfolio))
print(max(s['shares'] * s['price'] for s in portfolio))


s = ('GOOG', 100, 490, 10)
print(','.join(str(c)for c in s))

# saving a lot of memory
import tracemalloc
import readrides
tracemalloc.start()
rows = readrides.read_rides_as_dict('../../Data/ctabus.csv')
rt22 = [row for row in rows if row['route'] == '22']
print(max(rt22, key=lambda row: row['rides']))
print(tracemalloc.get_traced_memory())

tracemalloc.start()
f = open('../../Data/ctabus.csv')
f_csv = csv.reader(f)
headers = next(f_csv)
rows = (dict(zip(headers, row)) for row in f_csv)
rt22 = (row for row in rows if row['route'] == '22')
print(max(rt22, key=lambda row: row['rides']))
print(tracemalloc.get_traced_memory())
