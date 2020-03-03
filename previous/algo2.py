test_str = ['' for i in range(50)]

def matching(card, word):
	pos = 0
	while pos<len(card) and pos<len(word) and (card[pos] == '?' or word[pos] == card[pos]):
		pos+=1

	if pos==len(card): return pos==len(word)

	if card[pos] == '*':
		skip=0
		while pos+skip<len(word):
			if matching(card[pos+1:],word[pos+skip:]): return True
			skip+=1

	return False

#input
f = open("input2.txt", 'r')
num_case = int(f.readline())

for test in range(num_case):
	pattern = f.readline()
	num_str = int(f.readline())

	print("Case "+str(test)+": ")
	for n in range(num_str):
		test_str[n] = f.readline()
		print(matching(pattern,test_str[n]))

f.close()