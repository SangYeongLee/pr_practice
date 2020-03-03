f = open("input4.txt", 'r')
num_case = int(f.readline())
instr = [[] for i in range(num_case)]
for i in range(num_case):
	buff = f.readline().split()
	for j in range(len(buff)):
		instr[i].append(int(buff[j]))

def lis(seq):
	longest = 0
	if len(seq)==0: return 0
	
	for j in range(len(seq)):
		temp = []
		for i in range(len(seq)-j-1):
			if seq[j+i+1]>seq[j]: 
				temp.append(seq[i+1])

		longest=max(longest,1+lis(temp))

	return longest

def lisfor(seq):
	if len(seq)==0: return []

	cache=[0 for i in range(len(seq))]
	cache[0]=1
	ret=1
	for i in range(len(seq)-1):
		for j in range(i+1):
			if seq[i+1]>seq[j] and cache[i+1]<cache[j]+1:
				cache[i+1]=1+cache[j]
			if cache[i+1]>ret: ret=cache[i+1]

	return ret

for i in range(num_case):
	print(lisfor(instr[i]))

f.close()