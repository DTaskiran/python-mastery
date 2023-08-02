# pcost.py

with open('../../Data/portfolio.dat', 'r') as f:
	port_list = [line[:-1].split(' ') for line in f.readlines()]

total_price = 0
for stock, num, price in port_list:
	total_price += int(num)*float(price)
print(total_price)
