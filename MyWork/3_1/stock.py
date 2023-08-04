# stock.py      
import csv
from sys import intern

class Stock:
    __slots__ = ['name', 'shares', 'price']
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    
    def cost(self):
        return self.shares * self.price
    
    def sell(self, amount):
        self.shares -= amount
        return self.shares

def read_portfolio(filename):
    portfolio = []
    with open(filename, 'r') as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        for name, shares, price in f_csv:
            portfolio.append(Stock(intern(name), int(shares), float(price)))
    return portfolio

def print_portfolio(portfolio):
    print(*[f'%10s' % s for s in Stock.__slots__])
    print('---------- '*3)
    for stock in portfolio:
        print('%10s %10s %10.2f' % (stock.name, stock.shares, stock.price))
