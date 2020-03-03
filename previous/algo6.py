import math

f= open("input6.txt",'r')
num_case = int(f.readline())

def sub_cal(s):
	if len(s)>0 and len(s)<3:
		return math.inf
	if len(s) == 0:
		return 0

	if s == [ s[0] for i in range(len(s))]:
		return 1

	prog = True
	for i in range(len(s)-2):
		if not s[i+1]-s[i] == s[i+2]-s[i+1]: prog = False
	
	if prog: 
		if abs(s[1]-s[0]) == 1:
			return 2
		else:
			return 5
	
	alter = True
	for i in range(2,len(s)):
		if not s[i]==s[i%2]: alter=False

	if alter: return 4

	return 10


def cal_point(idx):
	global seq
	global cache

	if not cache[idx]==-1: return cache[idx]

	if len(seq[idx:])==0: 
		cache[idx]=0
		return 0
	elif len(seq[idx:])<3 and len(seq[idx:])>0: 
		cache[idx]=math.inf
		return math.inf
	elif len(seq[idx:])>=3 and len(seq[idx:])<=5: 
		cache[idx]=sub_cal(seq[idx:])
		return sub_cal(seq[idx:])
	else :
		cache[idx]=min([sub_cal(seq[idx:idx+3])+cal_point(idx+3),
			sub_cal(seq[idx:idx+4])+cal_point(idx+4),
			sub_cal(seq[idx:idx+5])+cal_point(idx+5)])
		return cache[idx]

for i in range(num_case):
	seq = []
	cache=[]
	buff = f.readline()

	for j in range(len(buff)-1):
		seq.append(int(buff[j]))
		cache.append(-1)

	print("ans::"+str(cal_point(0)))
	print(cache)
f.close()