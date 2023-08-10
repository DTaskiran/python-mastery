# reader.py

import sys
import csv
import collections
from collections import defaultdict
from abc import ABC, abstractmethod

def read_csv_as_dicts(filename, types=[str, int, float]):
	"""
	Read filename from csv file into list of dictionaries, casting values to provided types
	"""
	parser = DictCSVParser(types)
	return parser.parse(filename)

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
	parser = InstanceCSVParser(cls)
	return parser.parse(filename)

class CSVParser(ABC):
	
	def parse(self, filename):
		records = []
		with open(filename) as f:
			rows = csv.reader(f)
			headers = next(rows)
			for row in rows:
				record = self.make_record(headers, row)
				records.append(record)
		return records
	
	@abstractmethod
	def make_record(self, headers, row):
		pass

class DictCSVParser(CSVParser):
	def __init__(self, types):
		self.types = types
	
	def make_record(self, headers, row):
		return {name:func(val) for name, func, val in zip(headers, self.types, row)}
class InstanceCSVParser(CSVParser):
	def __init__(self, cls):
		self.cls = cls
	
	def make_record(self, headers, row):
		return self.cls.from_row(row)
	

if __name__ == '__main__':
	from sys import intern
	import tracemalloc

	filename = '../../Data/ctabus.csv'
	types = [intern, intern, intern, int]

	tracemalloc.start()
	data = read_csv_as_columns(filename, types)
	print(tracemalloc.get_traced_memory())
	print(data[0])

