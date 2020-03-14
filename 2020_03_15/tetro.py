#https://www.acmicpc.net/problem/14500
temp = input().split()
N,M = int(temp[0]),int(temp[1])

board = [[0 for j in range(M+2)] for i in range(N+2)]
for i in range(N):
	temp = input().split()
	for j in range(M):
		board[i+1][j+1] = int(temp[j])

tetro14 = [ [[0,0],[0,1],[0,2],[0,3]] ]
tetro22 = [ [[0,0],[0,1],[1,0],[1,1]] ]
tetro23 = [ [[0,0],[1,0],[1,1],[1,2]], [[0,1],[1,0],[1,1],[1,2]], [[0,2],[1,0],[1,1],[1,2]],
			[[0,0],[0,1],[0,2],[1,0]], [[0,0],[0,1],[0,2],[1,1]], [[0,0],[0,1],[0,2],[1,2]],
			[[0,0],[0,1],[1,1],[1,2]], [[1,0],[1,1],[0,1],[0,2]]]
tetro32 = [ [[0,0],[1,0],[2,0],[0,1]], [[0,0],[1,0],[2,0],[1,1]], [[0,0],[1,0],[2,0],[2,1]],
			[[0,1],[1,1],[2,1],[0,0]], [[0,1],[1,1],[2,1],[1,0]], [[0,1],[1,1],[2,1],[2,0]],
			[[0,0],[1,0],[1,1],[2,1]], [[0,1],[1,0],[1,1],[2,0]]]
tetro41 = [ [[0,0],[1,0],[2,0],[3,0]] ]

ans=0
for i in range(1,N+1):
	for j in range(1,M-2):
		for shape in tetro14:
			temp=0
			for block in shape:
				temp+=board[i+block[0]][j+block[1]]
			if temp>ans: ans = temp

for i in range(1,N):
	for j in range(1,M):
		for shape in tetro22:
			temp = 0
			for block in shape:
				temp+=board[i+block[0]][j+block[1]]
			if temp>ans: ans = temp

for i in range(1,N):
	for j in range(1,M-1):
		for shape in tetro23:
			temp = 0
			for block in shape:
				temp+=board[i+block[0]][j+block[1]]
			if temp>ans: ans = temp

for i in range(1,N-1):
	for j in range(1,M):
		for shape in tetro32:
			temp = 0
			for block in shape:
				temp+=board[i+block[0]][j+block[1]]
			if temp>ans: ans = temp

for i in range(1,N-2):
	for j in range(1,M+1):
		for shape in tetro41:
			temp = 0
			for block in shape:
				temp+=board[i+block[0]][j+block[1]]
			if temp>ans: ans = temp

print(ans)