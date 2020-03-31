#https://www.acmicpc.net/problem/18808

def stk_on(board, sticker, a, b):
	for i in range(len(sticker)):
		for j in range(len(sticker[0])):
			if sticker[i][j]==1 and board[a+i][b+j]==1:
				return False
	return True

def rotate(stk):
	n, m = len(stk), len(stk[0])
	ret = [[stk[n-i-1][j] for i in range(n)] for j in range(m)]

	return ret

temp = list(map(int,input().split()))

n, m, k = temp[0], temp[1], temp[2]

notebook = [[0 for i in range(m)] for j in range(n)]

ans=0
for stk in range(k):
	temp = input().split()
	a, b = int(temp[0]), int(temp[1])

	stk = []
	for i in range(a):
		stk.append( list(map(int, input().split())) )

	for r in range(4):
		flag = False
		a, b = len(stk), len(stk[0])
		s1, s2 = 0, 0

		for i in range(n-a+1):
			for j in range(m-b+1):
				if stk_on(notebook,stk,i,j): 
					flag = True
					s1, s2 = i, j
					break
			if flag:
				break

		if flag:
			for i in range(a):
				for j in range(b):
					if stk[i][j]==1: 
						ans+=1
						notebook[s1+i][s2+j]=stk[i][j]
			break

		stk = rotate(stk)

print(ans)