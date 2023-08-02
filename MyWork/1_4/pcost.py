# pcost.py

def portfolio_cost(path_to_portfolio):
	with open(path_to_portfolio, 'r') as f:
		total_price = 0
		for line in f:
			line = line.replace('  ', ' ')[:-1]
			stock, num, price = line.split(' ')
			try: 
				total_price += int(num)*float(price)
			except ValueError as e: 
				print(f'Could not parse: {stock, num, price}')
				print(f'Reason: {e}')
	return total_price

print(portfolio_cost('../../Data/portfolio3.dat'))
