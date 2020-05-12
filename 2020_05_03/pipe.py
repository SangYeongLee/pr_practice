def ret_shape(pipe):
	if pipe[0][0]==pipe[1][0] and pipe[1][1]-pipe[0][1]==1:
		return 0 #parallel
	elif pipe[0][1]==pipe[1][1] and pipe[1][0]-pipe[0][0]==1:
		return 1 #orthogonal
	else:
		return 2 #diagonal

n = int(input())

board = [[1 for _ in range(n+2)]]+\
		[[1]+list(map(int,input().split()))+[1] for _ in range(n)]+\
		[[1 for _ in range(n+2)]]

chk_para = [[(0,1)],[(0,1),(1,0),(1,1)]]
chk_orth = [[(1,0)],[(0,1),(1,0),(1,1)]]
chk_diag = [[(0,1)],[(1,0)],[(0,1),(1,0),(1,1)]]

stack = [[[1,1],[1,2]]]
route = 0

while len(stack)>0:
	pipe = stack.pop()
	if pipe[1] == [n,n]:
		route+=1
		continue
	shape = ret_shape(pipe)

	if shape==0:
		for move in chk_para:
			flag = True
			for chk in move:
				r,c = pipe[1][0]+chk[0], pipe[1][1]+chk[1]
				if board[r][c]!=0:
					flag=False
					break
			if flag:
				stack.append([pipe[1],[pipe[1][0]+move[-1][0], pipe[1][1]+move[-1][1]]])
	elif shape==1:
		for move in chk_orth:
			flag = True
			for chk in move:
				r,c = pipe[1][0]+chk[0], pipe[1][1]+chk[1]
				if board[r][c]!=0:
					flag=False
					break
			if flag:
				stack.append([pipe[1],[pipe[1][0]+move[-1][0], pipe[1][1]+move[-1][1]]])
	else:
		for move in chk_diag:
			flag = True
			for chk in move:
				r,c = pipe[1][0]+chk[0], pipe[1][1]+chk[1]
				if board[r][c]!=0:
					flag=False
					break
			if flag:
				stack.append([pipe[1],[pipe[1][0]+move[-1][0], pipe[1][1]+move[-1][1]]])
	print(stack)

print(route)