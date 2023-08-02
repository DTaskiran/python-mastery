# data analysis challenge

import readrides
from collections import Counter
rows = readrides.read_rides_as_dict('../../Data/ctabus.csv')

# Question 1
print('How many bus routes exist in Chicago?')
n_routs = len({s['route'] for s in rows})
print(f'{n_routs=}')

# Question 2
print('How many people rode the number 22 bus on Februrary 2, 2011')
n_rides = sum([s['rides'] for s in rows if (s['day'] == '02/02/2011' and s['route'] == '22')])
print(f'{n_rides=}')

# Question 3
print('What is the total number of rides taken on each bus route?')
rides_per_route = Counter()
for ride in rows:
	rides_per_route[ride['route']] += ride['rides']

# Make a table showing the routes and a count ranked by popularity !! copied from solutions
for route, count in rides_per_route.most_common(3):
    print('%5s %10d' % (route, count))

# Question 4
print('What five bus routes had the greatest ten-year increase in ridership from 2001 to 2011?')
rides_per_route_01 = Counter()
rides_per_route_11 = Counter()
for ride in rows:
	if '/2001' in ride['day']:
		rides_per_route_01[ride['route']] += ride['rides']
	elif '/2011' in ride['day']:
		rides_per_route_11[ride['route']] += ride['rides']

rides_delta = Counter()
for key, v11 in rides_per_route_11.items():
	v01 = rides_per_route_01[key]
	rides_delta[key] += v11 - v01
print(f'Top 5 routes with the greatest ten-year increase')
for route, count in rides_delta.most_common(5):
    print('%5s %10d' % (route, count))
