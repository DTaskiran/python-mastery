# memalloc behavior
# working in here instead of python3 interactive shell

import sys
import csv

print('list growth')
items = []
print('0 items in list: ', sys.getsizeof(items))

for i in range(1, 6):
	items.append(i)
	print(i, sys.getsizeof(items))

print('dict / class growth')
row = { 'route': '22', 'date': '01/01/2001', 'daytype': 'U', 'rides': 7354 }
print(len(row), sys.getsizeof(row))
row['a'] = 1
print(len(row), sys.getsizeof(row))
row['b'] = 2
print(len(row), sys.getsizeof(row))
del row['b']
print('deleted one item, memory usage remains unchanged')
print(len(row), sys.getsizeof(row))

print('chaning orientation to columns')
print('continued in read_cols.py file')
