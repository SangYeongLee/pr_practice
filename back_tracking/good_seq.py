#https://www.acmicpc.net/problem/2661
def chk_bad(seq):
	n = 0
	for c in seq:
		if c=='0': break
		else: n+=1

	for num in range(1,n//2+1):
		flag = True
		for i in range(num):
			if seq[n-i-1]!=seq[n-num-i-1]:
				flag = False
				break

		if flag: return flag
	return False

def make_seq(cur):
	if n-1==cur:
		for i in range(1,4):
			seq[cur] = str(i)
			if not chk_bad(seq): 
				print("".join(seq))
				exit()
			seq[cur] = '0'
	else:
		for i in range(1,4):
			seq[cur] = str(i)
			if not chk_bad(seq): make_seq(cur+1)
			seq[cur] = '0'

n = int(input())
seq = ['0' for _ in range(n)]
make_seq(0)
