#https://www.acmicpc.net/problem/12100
from collections import deque

def move(board,N):
	ret = []

	#left
	temp = []
	for i in range(N):
		combined = []
		que = deque()
		for j in range(N):
			if board[i][j] == 0: continue

			que.append(board[i][j])
			if len(que) == 2:
				if que[0]==que[1]:
					combined.append(que[0]*2)
					que=deque()
				else:
					combined.append(que.popleft())

		while len(combined)<N:
			if len(que)!=0:
				combined.append(que.popleft())
			else:
				combined.append(0)
			
		temp.append(combined)
	ret.append(temp)

	#right
	temp = []
	for i in range(N):
		combined = []
		que = deque()
		for j in range(N-1,-1,-1):
			if board[i][j] == 0: continue

			que.append(board[i][j])
			if len(que) == 2:
				if que[0]==que[1]:

					combined.append(que[0]*2)
					que=deque()
				else:
					combined.append(que.popleft())

		while len(combined)<N:
			if len(que)!=0:
				combined.append(que.popleft())
			else:
				combined.append(0)
			
		temp.append(combined[::-1])
	ret.append(temp)

	#up
	temp = [[0 for i in range(N)] for j in range(N)]
	for j in range(N):
		combined = []
		que = deque()
		for i in range(N):
			if board[i][j] == 0: continue

			que.append(board[i][j])
			if len(que) == 2:
				if que[0]==que[1]:
					combined.append(que[0]*2)
					que=deque()
				else:
					combined.append(que.popleft())

		n=0
		for m in combined:
			temp[n][j] = m
			n+=1
		while len(que)!=0:
			temp[n][j] = que.popleft()
			n+=1
	ret.append(temp)

	#down
	temp = [[0 for i in range(N)] for j in range(N)]
	for j in range(N):
		combined = []
		que = deque()
		for i in range(N-1,-1,-1):
			if board[i][j] == 0: continue

			que.append(board[i][j])
			if len(que) == 2:
				if que[0]==que[1]:
					combined.append(que[0]*2)
					que=deque()
				else:
					combined.append(que.popleft())

		n=N-1
		for m in combined:
			temp[n][j] = m
			n-=1
		while len(que)!=0:
			temp[n][j] = que.popleft()
			n-=1
	ret.append(temp)

	return ret

# board안에 가장 큰 block 숫자 구하는 함수
def max_block(board,N):
	ret = 0
	for row in board:
		for val in row:
			if ret<val: ret = val

	return ret

N = int(input())

board = [[0 for i in range(N)] for j in range(N)]
for i in range(N):
	temp = input().split()
	for j in range(N):
		board[i][j] = int(temp[j])

stack = [(board,0)]
answer = 0

#dfs
while len(stack)!=0:
	temp = stack.pop()
	if temp[1]==5:
		if answer<max_block(temp[0],N): 
			answer = max_block(temp[0],N)
		continue

	for m in move(temp[0],N):
		stack.append((m,temp[1]+1))

print(answer)