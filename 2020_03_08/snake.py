from collections import deque

#입출력
n = int(input())
k = int(input())

#board 경계는 1로 채움
board = [[0 for i in range(n+2)] for j in range(n+2)]
for i in range(n+2):
	for j in range(n+2):
		if i==0 or j==0 or i==n+1 or j==n+1:
			board[i][j]=1
board[1][1]=2

apple = []
for i in range(k):
	temp = input().split()
	apple.append((int(temp[0]),int(temp[1])))

l = int(input())

move = {}
for i in range(l):
	temp = input().split()
	move[int(temp[0])] = temp[1]

turn=1
cur_direc=0	#현재 방향 index

#snake 좌표 리스트
lst = deque()
lst.append((1,1))

#방향 정보
direc = [(0,1),(1,0),(0,-1),(-1,0)]
while True:
	m = direc[cur_direc]
	num = len(lst)-1
	temp = lst.popleft()

	#게임이 끝난 경우
	if board[temp[0]+m[0]][temp[1]+m[1]]!=0: break
	flag = False

	#head 채움
	lst.append([temp[0]+m[0],temp[1]+m[1]])
	board[temp[0]+m[0]][temp[1]+m[1]]=2

	#사과를 먹은 경우
	if (temp[0]+m[0],temp[1]+m[1]) in apple: 
		flag=True
		apple.remove((temp[0]+m[0],temp[1]+m[1]))
	
	#snake 안의 head, tail 제외한 몸통 다 넣기
	for i in range(num):
		board[temp[0]][temp[1]]=2
		lst.append(temp)
		temp = lst.popleft()
	
	#사과를 먹었으면 tail 유지, 아니면 지움
	if not flag:
		board[temp[0]][temp[1]]=0
	else:
		lst.append(temp)
	
	#방향 전환
	if turn in move:
		if move[turn]=='D':
			cur_direc = (cur_direc+1)%4
		else:
			cur_direc = (cur_direc-1)%4
	turn+=1
print(turn)