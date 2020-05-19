#https://www.acmicpc.net/problem/2580
def solve(zeros):
	if len(zeros)==0:
		for i in range(9):
			for j in range(8):
				print(board[i][j],end=' ')
			print(board[i][8])
		exit()
	
	chk = [False for i in range(10)]
	idx = zeros[0]

	#parallel
	for i in range(9):
		if board[idx[0]][i]!=0:
			chk[board[idx[0]][i]]=True

	#vertical
	for i in range(9):
		if board[i][idx[1]]!=0:
			chk[board[i][idx[1]]]=True

	r,c = divide[(idx[0]//3)],divide[(idx[1]//3)]
	for i in range(r,r+3):
		for j in range(c,c+3):
			if board[i][j]!=0:
				chk[board[i][j]]=True

	for i in range(1,10):
		if not chk[i]:
			board[idx[0]][idx[1]] = i
			solve(zeros[1:])
			board[idx[0]][idx[1]] = 0

board = []
zeros = []
ans = []

for i in range(9):
	temp = list(map(int,input().split()))
	for j in range(9):
		if temp[j]==0:
			zeros.append([i,j])
	board.append(temp)

divide =[0,3,6]
solve(zeros)