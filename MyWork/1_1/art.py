# art.py 

import sys
import random

chars = "\|/"

def draw(rows, columns):
	for r in range(int(rows)):
		print(''.join(random.choice(chars) for _ in range(int(columns))))
	
if __name__ == '__main__':
	if len(sys.argv) != 3:
		raise SystemExit("Usage: art.py rows columns")
	draw(sys.argv[1], sys.argv[2])
