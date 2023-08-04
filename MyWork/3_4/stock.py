# stock.py      
import csv
from reader import read_csv_as_instance
from sys import intern

class Stock:
    _types = (str, int, float)
    __slots__ = ['name', '_shares', '_price']

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def shares(self):
        return self._shares
    
    @shares.setter
    def shares(self, value):
        dtype = self.__class__._types[self.__class__.__slots__.index('_shares')]
        if not isinstance(value, dtype):
            raise TypeError(f"Value must be of type {dtype.__name__}, got {type(value).__name__}")
        if not value >= 0:
            raise ValueError("Value must be non-negative")
        self._shares = value
        return self._shares

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        dtype = self.__class__._types[self.__class__.__slots__.index('_price')]
        if not isinstance(value, dtype):
            raise TypeError(f"Value must be of type {dtype.__name__}, got {type(value).__name__}")
        if not value >= 0:
            raise ValueError("Value must be non-negative")
        self._price = value
        return self._price

    @classmethod
    def from_row(cls, row):
        return cls(*[func(v) for func, v in zip(cls._types, row)])
    
    @property
    def cost(self):
        return self.shares * self.price
    
    def __repr__(self):
        return f'{self.name:<4} | {self.shares:5} u | {self.price:7} $/u'
    
    def sell(self, amount):
        self.shares -= amount
        return self.shares
    
from decimal import Decimal
class DStock(Stock):
    _types = (str, int, Decimal)

def print_portfolio(portfolio):
    print(*[f'%10s' % s for s in Stock.__slots__])
    print('---------- '*3)
    for stock in portfolio:
        print('%10s %10s %10.2f' % (stock.name, stock.shares, stock.price))


if __name__ == '__main__':
    portfolio = read_csv_as_instance('../../Data/portfolio.csv', Stock)
    