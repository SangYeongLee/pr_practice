#https://www.acmicpc.net/problem/17142
from itertools import combinations
from collections import deque

temp = input().split()
n, m = int(temp[0]), int(temp[1])

near = [[0,1],[1,0],[-1,0],[0,-1]]
virus = []
blank = 0
board = [[1 for i in range(n+2)] for j in range(n+2)]
for i in range(n):
	temp = input().split()
	for j in range(n):
		board[i+1][j+1] = int(temp[j])
		if board[i+1][j+1] == 2:
			virus.append([i+1,j+1])
		elif board[i+1][j+1] == 0:
			blank+=1

if blank==0:
	print(0)
	exit()
ans = 2501
for comb in combinations(virus,m):
	temp = [[c for c in row] for row in board]
	que = deque()
	for ele in comb:
		temp[ele[0]][ele[1]] = 3
		que.append(ele+[0])

	time = 0
	cnt=0
	flag = False
	while len(que)!=0:
		cur = que.popleft()

		for move in near:
			if temp[cur[0]+move[0]][cur[1]+move[1]]==0:
				if cur[2]+1>ans:
					flag = True
					break

				cnt+=1
				temp[cur[0]+move[0]][cur[1]+move[1]] = 3
				que.append([cur[0]+move[0],cur[1]+move[1],cur[2]+1])

				if cur[2]+1>time: time = cur[2]+1
				if cnt==blank:
					flag = True
					break
			elif temp[cur[0]+move[0]][cur[1]+move[1]]==2:
				temp[cur[0]+move[0]][cur[1]+move[1]] = 3
				que.append([cur[0]+move[0],cur[1]+move[1],cur[2]+1])

		if flag:
			break
	
	if time<ans and cnt==blank:
		ans = time

if ans == 2501:
	print(-1)
else:
	print(ans)
