#https://www.acmicpc.net/problem/1987
temp = input().split()
r, c = int(temp[0]), int(temp[1])

board = [['x' for i in range(c+2)] for j in range(r+2)]
for i in range(r):
	temp = input()
	for j in range(c):
		board[i+1][j+1] = temp[j]

alpha=dict()

for i in range(26):
	alpha[chr(65+i)] = i

visited = [0 for i in range(26)]
visited[alpha[board[1][1]]] = 1
stack = [[1,1,visited]]
ans = 1
move = [[1,0],[0,1],[-1,0],[0,-1]]

while len(stack)>0:
	cur = stack.pop()
	x,y = cur[0],cur[1]
	v = cur[2]
	prev_len = sum(v)

	ans = max(prev_len,ans)
	if ans==26:
		break

	for m in move:
		if board[x+m[0]][y+m[1]]!='x' and v[alpha[board[x+m[0]][y+m[1]]]]==0:
			new_v = [i for i in v]
			new_v[alpha[board[x+m[0]][y+m[1]]]] = 1
			stack.append([x+m[0],y+m[1],new_v])

print(ans)