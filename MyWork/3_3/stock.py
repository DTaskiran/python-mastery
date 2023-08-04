# stock.py      
import csv
from sys import intern

class Stock:
    __slots__ = ['name', 'shares', 'price']
    types = (str, int, float)

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @classmethod
    def from_row(cls, row):
        return cls(*[func(v) for func, v in zip(cls.types, row)])
    
    def cost(self):
        return self.shares * self.price
    
    def __repr__(self):
        return f'{self.name:<4} | {self.shares:5} u | {self.price:7} $/u'
    
    def sell(self, amount):
        self.shares -= amount
        return self.shares
    
from decimal import Decimal
class DStock(Stock):
    types = (str, int, Decimal)

def print_portfolio(portfolio):
    print(*[f'%10s' % s for s in Stock.__slots__])
    print('---------- '*3)
    for stock in portfolio:
        print('%10s %10s %10.2f' % (stock.name, stock.shares, stock.price))
