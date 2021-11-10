import sys
import math
import random

import re


def remove_connectors(s):
	return re.sub('[\'\"-]','',s)

def remove_saparators(s):
	return re.sub('[;.!?,\n]',' ',s)

def remove_numbers(s):
	return re.sub('[0-9]','',s)


if len(sys.argv) > 1:
	text = ''
	with open(sys.argv[1], 'r') as f:
		text = f.read()

	print('Original :\n',text)
	text = text.lower()
	text = remove_connectors(text)
	text = remove_saparators(text)
	text = remove_numbers(text)

	print('Refined :\n',text)

	map = [i for i in range(26)]
	random.shuffle(map)

	res = ''
	for i in range(len(text)):
		if text[i].islower():
			res += chr(map[ord(text[i])-ord('a')]+ord('a'))
		else :
			res += ' '

	print('Final :\n',res)



	with open(sys.argv[1], 'w') as f:
		f.write(res)



else :
	print('need an input file')
