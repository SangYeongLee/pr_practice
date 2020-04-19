def turn(direc):
	if direc==1 or direc==3:
		return direc+1
	else:
		return direc-1

def update(y, x, cur):
	global board, horse, stack
	
	#흰색
	if board[y][x]==0:
		#원래 스택에서 지움
		for h in range(len(horse)):
			if cur in stack[h] and cur!=h:
				stack[h] = stack[h][:stack[h].index(cur)]
		
		#이동한 스택에 붙임
		for h in range(len(horse)):
			if y == horse[h][0] and x == horse[h][1]:
				for val in stack[cur]:
					stack[h].append(val)

		# stack에 있는 애들 인덱스 바꿔주기
		for on in stack[cur]:
			horse[on][0], horse[on][1] = y, x
	#빨강
	elif board[y][x]==1:
		#원래 스택에서 지움
		for h in range(len(horse)):
			if cur in stack[h] and cur!=h:
				stack[h] = stack[h][:stack[h].index(cur)]
		
		#스택 뒤집어서 업데이트
		stack[cur].reverse()
		temp = [i for i in stack[cur]]
		for i in range(len(temp)):
			stack[temp[i]] = temp[i:]

		#이동한 스택에 붙임
		for h in range(len(horse)):
			if y == horse[h][0] and x == horse[h][1]:
				for val in temp:
					stack[h].append(val)

		# stack에 있는 애들 인덱스 바꿔주기
		for on in temp:
			horse[on][0], horse[on][1] = y, x
	
move = [(0,1),(0,-1),(-1,0),(1,0)]

temp = input().split()
n, m = int(temp[0]), int(temp[1])

board = [[2 for i in range(n+2)] for j in range(n+2)]
for i in range(n):
	temp = input().split()
	for j in range(n):
		board[i+1][j+1] = int(temp[j])

horse = []
stack = []
for i in range(m):
	horse.append(list(map(int,input().split())))
	stack.append([i])

# 0: white, red: 1, blue: 2
# >, <, ^, v
cnt=0
while cnt<=1000:
	for cur in range(len(horse)):
		y, x = horse[cur][0]+move[horse[cur][2]-1][0], horse[cur][1]+move[horse[cur][2]-1][1]
		
		#파랑일때
		if board[y][x]==2:
			horse[cur][2] = turn(horse[cur][2])
			y, x = horse[cur][0]+move[horse[cur][2]-1][0], horse[cur][1]+move[horse[cur][2]-1][1]

			#돌았을 때 파랑이면 넘어감
			if board[y][x]==2: 
				continue
			else:
				update(y,x,cur)
		else:
			#흰색 혹은 빨강
			update(y,x,cur)

		for h in stack:
			if len(h)>=4: 
				print(cnt+1)
				exit(0)
	cnt+=1
print(-1)
