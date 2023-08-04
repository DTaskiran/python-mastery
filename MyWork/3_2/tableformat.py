# tableformat.py

def print_table(objects, attributes):
	for att in attributes:
		print('%10s' % att, end=' ')
	print()
	for att in attributes:
		print('-'*10, end=' ')
	print()
	
	for obj in objects:
		for att in attributes:
			if hasattr(obj, att):
				print('%10s' % getattr(obj, att), end=' ')
			else:
				print('%10s' % '---', end=' ')
		print()
	print()

