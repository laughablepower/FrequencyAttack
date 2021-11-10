import sys
import re



def get_freq(s):
	s = re.sub("[^\w]", " ",  s)

	characters = {}
	for i in range(26):
		characters[str(chr(i+ord('a')))] = 0
	for i in s:
		if i.islower():
			characters[i] += 1


	words = {}
	for i in s.split():
		if len(i) not in words:
			words[len(i)] = {}
		if i in words[len(i)]:
			words[len(i)][i] += 1
		else:
			words[len(i)][i] = 1

	return characters , words





def start(text):
	print(text)
	ch ,wd = get_freq(text)

	for k in sorted(ch):
		print(k,ch[k])

	for k in sorted(wd):
		print(k)
		lst = wd[k]
		for w in sorted(lst):
			print(w,lst[w])






def main():
	if len(sys.argv) > 1:
		with open(sys.argv[1], 'r') as f:
			text = f.read()
			start(text)
	else:
		print('need filename')

if __name__ == '__main__':
	main()
