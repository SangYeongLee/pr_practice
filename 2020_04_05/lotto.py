#https://www.acmicpc.net/problem/6603
def comb(lst,n):
	ret = []
	if n > len(lst): return ret
	
	if n == 1:
		for i in lst:
			ret.append([i])
	elif n>1:
		for i in range(len(lst)-n+1):
			for temp in comb(lst[i+1:],n-1):
				ret.append([lst[i]]+temp)

	return ret

while True:
	temp = list(map(int,input().split()))
	n = temp[0]
	if n == 0: break

	num = temp[1:]

	for ans in comb(num,6):
		for num in ans:
			print(num,end=' ')
		print()
	print()