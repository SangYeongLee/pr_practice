#https://www.acmicpc.net/problem/15685

def draw_curve(board, start, d, g):
	direc = [(1,0),(0,-1),(-1,0),(0,1)]
	lst = [ [start[0],start[1]], [start[0]+direc[d][0],start[1]+direc[d][1]] ]
	
	for i in range(g):
		base = lst[-1]
		
		for point in reversed(lst[:-1]):
			lst.append([base[0]-(point[1]-base[1]),base[1]+(point[0]-base[0])])

	for idx in lst:
		board[idx[1]][idx[0]] = 1

n = int(input())
board = [[0 for i in range(101)] for j in range(101)]

for i in range(n):
	temp = list(map(int,input().split()))
	x, y, d, g = temp[0], temp[1], temp[2], temp[3]
	draw_curve(board, [x,y], d, g)

ans = 0
for i in range(100):
	for j in range(100):
		if board[i][j]==1 and board[i+1][j]==1 and board[i][j+1]==1 and board[i+1][j+1]==1:
			ans+=1
print(ans)