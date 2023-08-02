# readport.py

import csv
from pprint import pprint

#  A function that reads a file into a list of dicts
def read_portfolio(filename):
	portfolio = []
	with open(filename, 'r') as f:
		rows = csv.reader(f)
		header = next(rows)
		for row in rows:
			record = {
				'name': row[0],
				'shares': int(row[1]),
				'price': float(row[2])
			}
			portfolio.append(record)
	return portfolio

if __name__ == '__main__':
	portfolio  = read_portfolio('../../Data/portfolio.csv')
	pprint(portfolio)

	## Comprehensions 
	# find all holdings more than 100 shares
	pprint([s for s in portfolio if s['shares'] > 100])

	# compute total cost (shares * price)
	pprint(sum([s['shares']*s['price'] for s in portfolio]))

	# find all unique stock names
	pprint({s['name'] for s in portfolio})

	# count total shares of each stock
	totals = {s['name']:0 for s in portfolio}
	for s in portfolio:
		totals[s['name']] += s['shares']
	pprint(totals)


	## Collections
	# same with Counter
	from collections import Counter
	totals = Counter()
	for s in portfolio:
		totals[s['name']] += s['shares']
	print(totals)

	# find two  most common
	print(totals.most_common(2))

	# adding counters together
	# simulated new purchases
	more = Counter()
	more['IBM'] = 75
	more['AA'] = 200
	more['ACME'] = 30
	pprint(f'{more=}')
	print(totals + more)

	# grouping data by name
	from collections import defaultdict
	byname = defaultdict(list)
	for s in portfolio:
		byname[s['name']].append(s)
	pprint(byname)
