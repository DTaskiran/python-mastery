# reader.py

import sys
import csv
import collections
from collections import defaultdict

def read_csv_as_dicts(filename, types=[str, int, float]):
	"""
	Read filename from csv file into list of dictionaries, casting values to provided types
	"""
	with open(filename, 'r') as f:
		f_csv = csv.reader(f)
		headers = next(f_csv)
		output = []
		for line in f_csv:
			output.append({h:func(v) for h, func, v in zip(headers, types, line)})
		return output

class DataCollections(collections.abc.Sequence):
	def __init__(self, columns):
		self.column_names = list(columns.keys())
		self.column_values = list(columns.values())
	
	def __len__(self):
		return len(self.column_values[0])
	
	def __getitem__(self, key):
		return {h:v[key] for h, v in zip(self.column_names, self.column_values)}

def read_csv_as_columns(filename, types=[str, int, float]):
	"""
	Read csv from filename and cast values to specified types
	return datacollections object
	"""
	cols = defaultdict(list)
	with open(filename, 'r') as f:
		f_csv = csv.reader(f)
		headers = next(f_csv)
		for line in f_csv:
			[cols[h].append(func(v)) for h, func, v in zip(headers, types, line)]
	return DataCollections(cols)

def read_csv_as_instance(filename, cls):
	"""
	Read a CSV file into a list of instances of a given class
	"""
	output = []
	with open(filename, 'r') as f:
		f_csv = csv.reader(f)
		headers = next(f_csv)
		for line in f_csv:
			output.append(cls.from_row(line))
	return output

if __name__ == '__main__':
	from sys import intern
	import tracemalloc

	filename = '../../Data/ctabus.csv'
	types = [intern, intern, intern, int]

	tracemalloc.start()
	data = read_csv_as_columns(filename, types)
	print(tracemalloc.get_traced_memory())
	print(data[0])

