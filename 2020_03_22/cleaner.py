#https://www.acmicpc.net/problem/14889
def left(direc):
	return (direc-1)%4

#0:북, 1:동, 2:남 3:서
buff = input().split()
N,M = int(buff[0]), int(buff[1])

buff = input().split()
r,c,direc = int(buff[0])+1, int(buff[1])+1, int(buff[2])

move = [(-1,0),(0,1),(1,0),(0,-1)]
board = [[1 for i in range(M+2)] for j in range(N+2)]
for i in range(N):
	buff = input().split()
	for j in range(M):
		board[i+1][j+1] = int(buff[j])

answer = 0

while True:
	if board[r][c]==0:
		board[r][c]=2
		answer+=1

	#네 방향 체크
	next_d=left(direc)
	for i in range(4):
		if board[r+move[next_d][0]][c+move[next_d][1]]==0:
			break
		next_d = left(next_d)

	if next_d == left(direc) and board[r+move[next_d][0]][c+move[next_d][1]]!=0:
		#네 방향 모두 청소 or 벽 + 뒤쪽도 벽
		if board[r-move[direc][0]][c-move[direc][1]]==1:
			break
		#뒤쪽이 벽이 아닌 경우 후진
		else:
			r = r-move[direc][0]
			c = c-move[direc][1]
	#청소할 곳 찾았을 때
	else:
		direc = next_d
		r += move[direc][0]
		c += move[direc][1]

print(answer)