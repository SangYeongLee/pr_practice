f=open("input5.txt",'r')
num_case = int(f.readline())

def jlis(idx1,idx2):
	global s1,s2
	if not cache[idx1+1][idx2+1]==-1: return cache[idx1+1][idx2+1]

	return 1

for i in range(num_case):
	buff = f.readline().split()
	size1=int(buff[0])
	size2=int(buff[1])
	buff = f.readline().split()
	cache=[[-1 for a in range(size1+1)] for b in range(size2+1)]
	s1=[]
	s2=[]
	for j in range(size1):
		s1.append(int(buff[j]))
	buff = f.readline().split()
	for j in range(size2):
		s2.append(int(buff[j]))
	
	print(jlis(-1,-1))


f.close()