#https://www.acmicpc.net/problem/17140
#transpose
def trans(board):
	temp = [[board[i][j] for i in range(len(board))] for j in range(len(board[0]))]

	return temp

#R operation
def r_op(board):
	size = 0
	for i in range(len(board)):
		#수의 등장 횟수 체크
		cnt = dict()
		for j in range(len(board[i])):
			# 0의 등장 횟수는 제외
			if board[i][j]==0: continue

			if board[i][j] not in cnt:
				cnt[board[i][j]]=1
			else:
				cnt[board[i][j]]+=1
		
		#정렬을 한 새로운 배열로 replace
		new_list = []
		
		for ele in sorted(cnt, key = lambda val : (cnt[val], val)):
			new_list.append(ele)
			new_list.append(cnt[ele])
		if len(new_list)>size: size = len(new_list)
		board[i] = new_list
	
	# 가장 긴 행의 길이에 맞게 행에 0을 추가
	for i in range(len(board)):
		add_num = size-len(board[i])
		for j in range(add_num):
			board[i].append(0)

temp = input().split()
r,c,k = int(temp[0]),int(temp[1]),int(temp[2])

board = [[0 for i in range(3)] for j in range(3)]
for i in range(3):
	temp = input().split()
	for j in range(3):
		board[i][j] = int(temp[j])

time = 0
while True:
	#종료조건
	if r-1<len(board) and c-1<len(board[0]) and board[r-1][c-1]==k:
		break
	time+=1
	if time>100:
		break

	#R operation
	if len(board)>=len(board[0]):
		r_op(board)
	#C operation = transpose + R operation + transpose
	else:
		board=trans(board)
		r_op(board)
		board=trans(board)

if time>100:
	print(-1)
else:
	print(time)