#https://www.acmicpc.net/problem/16236
from collections import deque

# input
N = int(input())

shark = [0,0]
board = [[-1 for i in range(N+2)] for j in range(N+2)]
for i in range(N):
	temp = input().split()
	for j in range(N):
		board[i+1][j+1] = int(temp[j])
		if board[i+1][j+1] == 9:
			shark[0], shark[1] = i+1, j+1

ans = 0 # 시간 저장
size = 2 # 상어 size
cnt = 0 # 상어가 현재 size에서 몇 마리를 먹엇는지 저장하는 변수
move = [(-1,0),(0,-1),(0,1),(1,0)]

while True:
	# 방문 상태 저장하는 set
	visit = set()
	# queue에 [상어 r좌표, 상어 c좌표, 상어로 부터 거리] 형태로 enqueue
	que = deque()
	que.append(shark+[0])
	visit.add((shark[0],shark[1]))
	target = [0,0,0] # 다음에 먹을 물고기의 좌표와 거기까지 가는데 걸리는 시간

	while len(que)!=0:
		cur = que.popleft()
		# queue에서 target까지의 거리보다 큰 값이 나올 경우
		if cur[2]>target[2] and target[2]!=0:
			break

		# 먹을 수 있는 물고기일 나올 경우
		if 0<board[cur[0]][cur[1]]<size and board[cur[0]][cur[1]]!=9:
			# 처음 찾은 물고기일 경우 초기화
			if target[2]==0:
				target = cur
			else:
				# 거리가 같은 물고기가 여러 개일 경우
				if cur[0]<target[0]:
					target = cur
				elif cur[0]==target[0] and cur[1]<target[1]:
					target=cur

		# cur의 주변 좌표를 비교해서 size보다 작거나 같고 방문한 적이 없으면 enqueue
		for idx in move:
			if 0<=board[cur[0]+idx[0]][cur[1]+idx[1]]<=size and \
			(cur[0]+idx[0],cur[1]+idx[1]) not in visit:
				que.append([cur[0]+idx[0],cur[1]+idx[1],cur[2]+1])
				visit.add((cur[0]+idx[0],cur[1]+idx[1]))
	
	# 먹을 수 있는 물고기가 없을 경우
	if target[0]==0 and target[1]==0:
		break
	
	# 먹고나서 size 갱신
	if cnt+1==size:
		cnt, size = 0, size+1
	else:
		cnt+=1

	# 먹고나서 board 상태와 시간 갱신
	board[shark[0]][shark[1]] = 0
	board[target[0]][target[1]] = 9
	ans+=target[2]
	shark = [target[0],target[1]]
	
print(ans)