# readrides.py

"""
Note: reading Data/ctabus.csv into string with f.read() results in 
nominal / peak memory usage of 12 MB / 24 MB
whereas reading it into a list with f.readlines() results in
nominal / peak memory usage of 40-50 MB
"""

import csv
import tracemalloc
from dataclasses import dataclass
from collections import namedtuple

def tracemem(func, *args):
	print(func.__name__)
	tracemalloc.start()
	result = func(*args)
	print('Memory Use: Current: %d, Peak: %d' % tracemalloc.get_traced_memory())
	return result

def read_rides_as_tuples(filename):
	"""
	Read the bus ride data as a list of tuples
	"""
	records = []
	with open(filename) as f:
		rows = csv.reader(f)
		headings = next(rows)
		for row in rows:
			route, day, daytype, rides = row
			record = (route, day, daytype, int(rides))
			records.append(record)
	return records

def read_rides_as_dict(filename):
	"""
	Read the bus ride data as a list of dictionaries
	"""
	records = []
	with open(filename) as f:
		rows = csv.reader(f)
		headings = next(rows)
		for row in rows:
			route, day, daytype, rides = row
			record = {'route':route, 'day':day, 'daytype':daytype, 'rides':int(rides)}
			records.append(record)
	return records
	
def read_rides_as_class(filename):
	"""
	Read the bus ride data as a list of standard classes
	"""
	class Row: 
		def __init__(self, route, day, daytype, rides):
			self.route = route
			self.day = day
			self.daytype = daytype
			self.rides = rides

	records = []
	with open(filename) as f:
		rows = csv.reader(f)
		headings = next(rows)
		for row in rows:
			route, day, daytype, rides = row
			record = Row(route, day, daytype, int(rides))
			records.append(record)
	return records

def read_rides_as_dclass(filename):
	"""
	Read the bus ride data as a list of dataclass objects
	"""
	@dataclass
	class Row: 
		route: str
		day: str
		daytype: str
		rides: int

	records = []
	with open(filename) as f:
		rows = csv.reader(f)
		headings = next(rows)
		for row in rows:
			route, day, daytype, rides = row
			record = Row(route, day, daytype, int(rides))
			records.append(record)
	return records

def read_rides_as_slots(filename):
	"""
	Read the bus ride data as a list of slots classes
	"""
	class Row: 
		__slots__ = ['route', 'day', 'daytype', 'rides']
		def __init__(self, route, day, daytype, rides):
			self.route = route
			self.day = day
			self.daytype = daytype
			self.rides = rides

	records = []
	with open(filename) as f:
		rows = csv.reader(f)
		headings = next(rows)
		for row in rows:
			route, day, daytype, rides = row
			record = Row(route, day, daytype, int(rides))
			records.append(record)
	return records

def read_rides_as_named_tuple(filename):
	"""
	Read the bus ride data as a list of named tuples
	"""
	Row = namedtuple('Row', ['route', 'day', 'daytype', 'rides'])

	records = []
	with open(filename) as f:
		rows = csv.reader(f)
		headings = next(rows)
		for row in rows:
			route, day, daytype, rides = row
			record = Row(route, day, daytype, int(rides))
			records.append(record)
	return records

	

if __name__ == '__main__':
	filepath = '../../Data/ctabus.csv'
	tracemem(read_rides_as_tuples, filepath)
	tracemem(read_rides_as_dict, filepath)
	tracemem(read_rides_as_class, filepath)
	tracemem(read_rides_as_dclass, filepath)
	tracemem(read_rides_as_slots, filepath)
	tracemem(read_rides_as_named_tuple, filepath)
