# read by cols 

import csv
import tracemalloc 
import collections

def read_rides_as_columns(filename):
	'''
	Read the bus ride data into 4 lists, representing columns
	'''
	routes = []
	dates = []
	daytypes = []
	numrides = []
	with open(filename) as f:
		rows = csv.reader(f)
		headings = next(rows)     # Skip headers
		for row in rows:
			routes.append(row[0])
			dates.append(row[1])
			daytypes.append(row[2])
			numrides.append(int(row[3]))
	return list((routes, dates, daytypes, numrides))

def read_rides_as_dicts(filename):
    '''
    Read the bus ride data as a list of dicts
    '''
    records = RideData()      # <--- CHANGE THIS
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = {
                'route': route, 
                'date': date, 
                'daytype': daytype, 
                'rides' : rides
                }
            records.append(record)
    return records


class RideData(collections.abc.Sequence):
	def __init__(self):
		
		self.routes = []
		self.dates = []
		self.daytypes = []
		self.numrides = []

	def __len__(self):
		return len(self.routes)
	
	def __getitem__(self, index):
		if isinstance(index, int):
			return {'route': self.routes[index],
					'date': self.dates[index],
					'daytype': self.daytypes[index],
					'rides': self.numrides[index]}
		elif isinstance(index, slice):
			out = RideData()
			out.routes = self.routes[index]
			out.dates = self.dates[index]
			out.daytypes = self.daytypes[index]
			out.numrides = self.numrides[index]
			return out
		

	def append(self, d):
		self.routes.append(d['route'])
		self.dates.append(d['date'])
		self.daytypes.append(d['daytype'])
		self.numrides.append(d['rides'])

if __name__ == "__main__":
	tracemalloc.start()
	columns = read_rides_as_dicts('../../Data/ctabus.csv')
	print(tracemalloc.get_traced_memory())
