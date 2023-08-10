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

class ColumnFormatMixin:
    formats = []
    def row(self, rowdata):
        rowdata = [(fmt % d) for fmt, d in zip(self.formats, rowdata)]
        super().row(rowdata)
class UpperHeadersMixin:
    def headings(self, headers):
	    super().headings([h.upper() for h in headers])
	
def create_formatter(choice, column_formats=[], upper_headers=False):
	format_classes = []
	if upper_headers:
		format_classes.append(UpperHeadersMixin)
	if column_formats:
		format_classes.append(ColumnFormatMixin)

	if choice == 'text': format_classes.append(TextTableFormatter)
	elif choice == 'csv': format_classes.append(CSVTableFormatter)
	elif choice == 'html': format_classes.append(HTMLTableFormatter)
	else: raise NotImplementedError("Formatter not implemented")

	class PortfolioFormatter(*format_classes):
		formats = column_formats
	
	return PortfolioFormatter()

def print_table(objects, attributes, formatter):
	if not isinstance(formatter, TableFormatter):
		raise TypeError("Expected a TableFormatter")
	
	formatter.headings(attributes)
	for obj in objects:
		# validate attribute exists
		row_data = [getattr(obj,attr) if hasattr(obj,attr) else '---' for attr in attributes]
		formatter.row(row_data)

if __name__ == '__main__':
	import stock, reader
	portfolio = reader.read_csv_as_instance('../../Data/portfolio.csv', stock.Stock)
	
