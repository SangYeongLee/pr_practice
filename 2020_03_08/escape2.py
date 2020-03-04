from collections import deque

def move(board,red,blue):
	#down, right, up, left
	N = len(board)
	M = len(board[0])
	direction = [(1,0),(0,1),(-1,0),(0,-1)]
	ret = []

	for m in direction:
		#blue
		b=1
		while True:
			if board[blue[0]+b*m[0]][blue[1]+b*m[1]]=='#':
				b-=1
				break
			elif board[blue[0]+b*m[0]][blue[1]+b*m[1]]=='O':
				break
			b+=1

		#red
		r=1
		while True:
			if board[red[0]+r*m[0]][red[1]+r*m[1]]=='#':
				r-=1
				break
			elif board[red[0]+r*m[0]][red[1]+r*m[1]]=='O':
				break
			r+=1
		temp=[]
		if blue[0]+b*m[0]==red[0]+r*m[0] and blue[1]+b*m[1]==red[1]+r*m[1]:
			if board[red[0]+r*m[0]][red[1]+r*m[1]]!='O':
				if m[0]==1:
					if blue[0]<red[0]:
						temp = [[red[0]+r*m[0],red[1]],[blue[0]+b*m[0]-1,blue[1]]]
					else:
						temp = [[red[0]+r*m[0]-1,red[1]],[blue[0]+b*m[0],blue[1]]]
				elif m[0]==-1:
					if blue[0]<red[0]:
						temp = [[red[0]+r*m[0]+1,red[1]],[blue[0]+b*m[0],blue[1]]]
					else:
						temp = [[red[0]+r*m[0],red[1]],[blue[0]+b*m[0]+1,blue[1]]]
				elif m[1]==1:
					if blue[1]<red[1]:
						temp = [[red[0],red[1]+r*m[1]],[blue[0],blue[1]+b*m[1]-1]]
					else:
						temp = [[red[0],red[1]+r*m[1]-1],[blue[0],blue[1]+b*m[1]]]
				else:
					if blue[1]<red[1]:
						temp = [[red[0],red[1]+r*m[1]+1],[blue[0],blue[1]+b*m[1]]]
					else:
						temp = [[red[0],red[1]+r*m[1]],[blue[0],blue[1]+b*m[1]+1]]
			else:
				temp = [[red[0]+r*m[0],red[1]+r*m[1]],[red[0]+r*m[0],red[1]+r*m[1]]]
		else:
			temp.append([red[0]+r*m[0],red[1]+r*m[1]])
			temp.append([blue[0]+b*m[0],blue[1]+b*m[1]])

		ret.append(temp)
				
	return ret

def endChk(ball,hole):
	if ball[0]==hole and ball[1]!=hole:
		return True
	return False

N,M = input().split()
N = int(N)
M = int(M)

board = [['' for i in range(M)] for j in range(N)]

for i in range(N):
	temp = input()
	for j in range(M):
		if temp[j]=='R':
			red = [i,j]
			board[i][j] = '.'
		elif temp[j]=='B':
			blue = [i,j]
			board[i][j] = '.'
		elif temp[j]=='O':
			hole = [i,j]
			board[i][j] = temp[j]
		else:
			board[i][j] = temp[j]

que = deque()
que.append(([red,blue],0))

ans=-1
while len(que)!=0:
	cur = que.popleft()
	if endChk(cur[0],hole):
		ans = cur[1]
		break

	for i in move(board,cur[0][0],cur[0][1]):
		if cur[0]!=i and cur[1]<10 and i[1]!=hole:
			que.append((i,cur[1]+1))

print(ans)