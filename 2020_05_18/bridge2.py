#https://www.acmicpc.net/problem/17472

#dfs로 붙어있는 땅들 그룹화해서 리스트로 반환
def grouping(board):
	ret = []
	direc = [(1,0),(-1,0),(0,1),(0,-1)]
	temp = []
	n, m = len(board), len(board[0])
	#복사
	for i in range(n):
		temp.append(board[i][:])

	for i in range(n):
		for j in range(m):
			#1 찾으면 dfs로 붙어 있는거 다 찾음
			if temp[i][j]==1:
				stack = [(i,j)]
				temp[i][j]=0
				i_set = set()

				while len(stack)>0:
					cur = stack.pop()
					i_set.add(cur)

					for n1,n2 in direc:
						if 0<=cur[0]+n1<n and 0<=cur[1]+n2<m and temp[cur[0]+n1][cur[1]+n2]==1:
							stack.append((cur[0]+n1,cur[1]+n2))
							temp[cur[0]+n1][cur[1]+n2]=0 #그룹에 넣은건 0으로 마킹
				ret.append(i_set) #집합 형태로 리스트에 저장
	return ret

#두 섬간의 거리 반환(2 이하이거나 도달 못하면 1000 반환)
def calc_dist(board,sum1,sum2):
	ret = 1000
	for p1 in sum1:
		for p2 in sum2:
			if p1[0]==p2[0]:
				start = min(p1[1],p2[1])
				val = abs(p1[1]-p2[1])

				#두 지점사이에 1이 없어야댐
				for j in range(start+1,start+val):
					if board[p1[0]][j]==1:
						val = -1
						break

				#거리가 2이상인거만
				if val>2 and val-1<ret:
					ret = val-1
			elif p1[1]==p2[1]:
				start = min(p1[0],p2[0])
				val = abs(p1[0]-p2[0])
				for i in range(start+1,start+val):
					if board[i][p1[1]]==1:
						val = -1
						break
				if val>2 and val-1<ret:
					ret = val-1

	return ret

n, m = map(int,input().split())
board = []
for _ in range(n):
	board.append(list(map(int,input().split())))

island = grouping(board)
s = len(island)
matrix = [[1000 for _ in range(s)] for _ in range(s)]

#연결 상태를 나타내는 matrix만듬
for i in range(s):
	for j in range(i+1,s):
		val = calc_dist(board,island[i],island[j])
		matrix[i][j], matrix[j][i] = val, val

#mst 구하기
connected = [0]
ans = 0
while len(connected)<s:
	idx, val = 0, 1000
	for i in connected:
		for j in range(s):
			if j not in connected and matrix[i][j]<val:
				idx, val = j, matrix[i][j]
	if val == 1000:
		print(-1)
		exit()

	connected.append(idx)
	ans+=val

print(ans)