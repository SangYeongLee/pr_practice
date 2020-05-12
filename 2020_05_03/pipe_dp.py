def ret_shape(pipe):
	if pipe[0][0]==pipe[1][0] and pipe[1][1]-pipe[0][1]==1:
		return 0 #parallel
	elif pipe[0][1]==pipe[1][1] and pipe[1][0]-pipe[0][0]==1:
		return 1 #orthogonal
	else:
		return 2 #diagonal

def search(pipe):
	global board,dp
	shape = ret_shape(pipe)
	if dp[pipe[1][0]][pipe[1][1]][shape]!=-1:
		return dp[pipe[1][0]][pipe[1][1]][shape]

	# 파이프 모양에 따라서 체크해야하는 좌표
	chk_para = [[(0,1)],[(0,1),(1,0),(1,1)]]
	chk_orth = [[(1,0)],[(0,1),(1,0),(1,1)]]
	chk_diag = [[(0,1)],[(1,0)],[(0,1),(1,0),(1,1)]]

	ret = 0
	if shape==0:
		for move in chk_para:
			flag = True #체크하는 구역에 하나라도 있으면 false
			for chk in move:
				r,c = pipe[1][0]+chk[0], pipe[1][1]+chk[1]
				if board[r][c]!=0:
					flag=False
					break
			if flag:
				ret+=search([pipe[1],[pipe[1][0]+move[-1][0], pipe[1][1]+move[-1][1]]])
	elif shape==1:
		for move in chk_orth:
			flag = True
			for chk in move:
				r,c = pipe[1][0]+chk[0], pipe[1][1]+chk[1]
				if board[r][c]!=0:
					flag=False
					break
			if flag:
				ret+=search([pipe[1],[pipe[1][0]+move[-1][0], pipe[1][1]+move[-1][1]]])
	else:
		for move in chk_diag:
			flag = True
			for chk in move:
				r,c = pipe[1][0]+chk[0], pipe[1][1]+chk[1]
				if board[r][c]!=0:
					flag=False
					break
			if flag:
				ret+=search([pipe[1],[pipe[1][0]+move[-1][0], pipe[1][1]+move[-1][1]]])

	dp[pipe[1][0]][pipe[1][1]][shape] = ret
	return ret

n = int(input())

board = [[1 for _ in range(n+2)]]+\
		[[1]+list(map(int,input().split()))+[1] for _ in range(n)]+\
		[[1 for _ in range(n+2)]]

# 파이프 한 쪽 끝이 해당 좌표에 위치할 때, 끝까지 가는 수 저장 (가로,세로,대각 순) 
dp = [[[-1,-1,-1] for i in range(n+2)] for i in range(n+2)]
dp[n][n]=[1,1,1]

print(search([[1,1],[1,2]]))