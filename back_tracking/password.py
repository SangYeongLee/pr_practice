#https://www.acmicpc.net/problem/1759
def making(chars,l):
	ret = []
	if l==1:
		for c in chars:
			ret.append(c)
		return ret

	for i in range(len(chars)-l+1):
		for sub in making(chars[i+1:],l-1):
			ret.append(chars[i]+sub)

	return ret

def chk(password):
	essen = ['a','e','i','o','u']
	cnt = 0
	for c in password:
		if c in essen: cnt+=1

	if cnt>=1 and len(password)-cnt>=2:
		return True
	else:
		return False

temp = input().split()
L, C = int(temp[0]), int(temp[1])
ch = input().split()

ch = sorted(ch)
for ans in making(ch,L):
	if chk(ans): print(ans)