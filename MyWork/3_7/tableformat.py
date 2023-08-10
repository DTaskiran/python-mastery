# tableformat.py
from abc import ABC, abstractmethod

class TableFormatter(ABC):

	@abstractmethod
	def headings(self, headers):
		raise NotImplementedError()
	@abstractmethod
	def row(self, row):
		raise NotImplementedError()
	
class TextTableFormatter(TableFormatter):

	def headings(self, headers):
		for h in headers:
			print('%10s' % h, end=' ')
		print()
		for h in headers:
			print('-'*10, end=' ')
		print()
	
	def row(self, row):
		for v in row:
				print('%10s' % v, end=' ')
		print()

class CSVTableFormatter(TableFormatter):

	def headings(self, headers):
		print(','.join(str(h) for h in headers))
	def row(self, row):
		print(','.join(str(r) for r in row))

class HTMLTableFormatter(TableFormatter):

	def headings(self, headers):
		tds = ' '.join(f'<th>{str(h)}</th>' for h in headers)
		print(f'<tr> {tds} </tr>')
	
	def row(self, row):
		tds = ' '.join(f'<th>{str(d)}</th>' for d in row)
		print(f'<tr> {tds} </tr>')
	
def create_formatter(choice):
	if choice == 'text': return TextTableFormatter()
	if choice == 'csv': return CSVTableFormatter()
	if choice == 'html': return HTMLTableFormatter()
	raise NotImplementedError("Formatter not implemented")

def print_table(objects, attributes, formatter):
	if not isinstance(formatter, TableFormatter):
		raise TypeError("Expected a TableFormatter")
	
	formatter.headings(attributes)
	for obj in objects:
		# validate attribute exists
		row_data = [getattr(obj,attr) if hasattr(obj,attr) else '---' for attr in attributes]
		formatter.row(row_data)

if __name__ == '__main__':
	from reader import read_csv_as_instance
	from stock import Stock
	portfolio = read_csv_as_instance('../../Data/portfolio.csv', Stock)
	formatter = create_formatter('text')
	print_table(portfolio, Stock.__slots__, formatter)
