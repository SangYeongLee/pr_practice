import math
f= open("input7.txt",'r')

def quantize(idx,quan):
	global seq
	global cache
	ret=math.inf
	if not cache[quan-1][idx] == -1: return cache[quan-1][idx]

	if quan==1: return min_diff(seq[idx:])

	for i in range(idx,len(seq[idx:])-quan+idx+1):
		ret= min(quantize(i+1,quan-1)+min_diff(seq[idx:i+1]),ret) 
	cache[quan-1][idx]=ret
	return ret

def avg(seq):
	return round(sum(seq)/len(seq))

def min_diff(seq):
	ret=0
	mean=avg(seq)
	for i in seq:
		ret+=(i-mean)*(i-mean)
	
	return ret

num_case = int(f.readline())

for i in range(0,num_case):
	buff = f.readline().split()
	size = int(buff[0])
	quantum = int(buff[1])
	buff = f.readline().split()
	seq=[]
	for j in range(0,size):
		seq.append(int(buff[j]))
	seq.sort()
	cache = [[-1 for i in range(size)] for i in range(quantum)]
	print(quantize(0,quantum))

#print()5 37 13
f.close()