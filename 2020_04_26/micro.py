#https://www.acmicpc.net/problem/17144
def circ(R,C,upper,lower):
	up_dif = upper[0][0]-1
	low_dif = R-lower[0][0]
	for i in range(2,C+1):
		upper.append((upper[0][0],i))
		lower.append((lower[0][0],i))

	for i in range(up_dif):
		upper.append((upper[0][0]-i-1,C))
	for i in range(low_dif):
		lower.append((lower[0][0]+i+1,C))

	for i in range(C-1,0,-1):
		upper.append((1,i))
		lower.append((R,i))

	for i in range(up_dif-1):
		upper.append((i+2,1))
	for i in range(low_dif-1):
		lower.append((R-i-1,1))

R, C, T = map(int, input().split())

board = [[-1 for i in range(C+2)] for j in range(R+2)] 
cleaner = []
for i in range(R):
	temp = input().split()
	for j in range(C):
		board[i+1][j+1] = int(temp[j])
		if board[i+1][j+1]==-1:
			cleaner.append(i+1)

upper = [(cleaner[0],1)]
lower = [(cleaner[1],1)]
circ(R,C,upper,lower)
near = [(0,1),(0,-1),(1,0),(-1,0)]

for time in range(T):
	temp = [[-1]*(C+2)] +\
			[[-1] + [0]*C + [-1] for i in range(R)] +\
			[[-1]*(C+2)]
	
	for i in range(1,R+1):
		for j in range(1,C+1):
			if board[i][j]>0:
				cnt = 0
				one = board[i][j]//5
				for m in near:
					if board[i+m[0]][j+m[1]]!=-1:
						temp[i+m[0]][j+m[1]]+=one
						cnt+=1
				temp[i][j]+= board[i][j]-one*cnt
			elif board[i][j]==-1:
				temp[i][j]=-1

	#upper cleaner
	for idx in range(len(upper)-1,0,-1):
		if idx == 1:
			temp[upper[idx][0]][upper[idx][1]] = 0
		else:
			temp[upper[idx][0]][upper[idx][1]] = temp[upper[idx-1][0]][upper[idx-1][1]]

	#lower cleaner
	for idx in range(len(lower)-1,0,-1):
		if idx == 1:
			temp[lower[idx][0]][lower[idx][1]] = 0
		else:
			temp[lower[idx][0]][lower[idx][1]] = temp[lower[idx-1][0]][lower[idx-1][1]]

	board = temp

ans = 0
for i in range(1,R+1):
	for j in range(1,C+1):
		if board[i][j]>0:
			ans+=board[i][j]
print(ans)