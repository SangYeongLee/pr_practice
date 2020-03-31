#https://www.acmicpc.net/problem/15684

from itertools import combinations
import sys

def down(ladder, start):
	cur = start

	for row in ladder:
		if cur>0 and row[cur-1]==1:
			cur-=1
		elif cur<len(row) and row[cur]==1:
			cur+=1

	return cur

tmp = list(map(int,input().split()))

n,m,h = tmp[0],tmp[1],tmp[2]

ladder = [[0 for i in range(n-1)] for i in range(h)]

for i in range(m):
	tmp = list(map(int,input().split()))
	ladder[tmp[0]-1][tmp[1]-1] = 1

flag = True
for i in range(n):
	if down(ladder,i)!=i:
		flag=False
if flag:
	print(0)
	sys.exit(0)

add_list = []
for i in range(h):
	for j in range(n-1):
		if ladder[i][j]==1 or (j>0 and ladder[i][j-1]==1) or (j<n-2 and ladder[i][j+1]==1):
			continue
		else:
			add_list.append([i,j])

for num in range(1,4):
	if len(add_list)<num:
		break
	for lst in combinations(add_list,num):	
		flag = False
		
		for i in range(len(lst)):
			for j in range(i+1,len(lst)):
				if lst[i][0] == lst[j][0] and abs(lst[i][1]-lst[j][1])==1:
					flag = True
		if flag:
			continue
		
		for idx in lst:
			ladder[idx[0]][idx[1]] = 1
		
		flag = True
		for i in range(n):
			if down(ladder,i)!=i:
				flag = False
				break

		if flag:
			print(num)
			sys.exit(0)

		for idx in lst:
			ladder[idx[0]][idx[1]] = 0
print(-1)