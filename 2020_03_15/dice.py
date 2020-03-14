#https://www.acmicpc.net/problem/14499
temp = input().split()
N, M = int(temp[0]), int(temp[1])
x, y = int(temp[2])+1, int(temp[3])+1
num = int(temp[4])

board = [[-1 for j in range(M+2)] for i in range(N+2)]
for i in range(N):
	temp = input().split()
	for j in range(M):
		board[i+1][j+1] = int(temp[j])

class dice:
	def __init__(self):
		self.up = 0
		self.down = 0
		self.front = 0
		self.back = 0
		self.right = 0
		self.left = 0

	# 동쪽
	def move1(self,board,x,y):
		swap = self.down
		if board[x][y] == 0:
			board[x][y] = self.right
			self.down = self.right
		else:
			self.down = board[x][y]
			board[x][y] = 0
		
		self.right = self.up
		self.up = self.left
		self.left = swap

	# 서쪽
	def move2(self,board,x,y):
		swap = self.down

		if board[x][y] == 0:
			board[x][y] = self.left
			self.down = self.left
		else:
			self.down = board[x][y]
			board[x][y] = 0
		
		self.left = self.up
		self.up = self.right
		self.right = swap

	# 북쪽
	def move3(self,board,x,y):
		swap = self.down

		if board[x][y] == 0:
			board[x][y] = self.back
			self.down = self.back
		else:
			self.down = board[x][y]
			board[x][y] = 0
		
		self.back = self.up
		self.up = self.front
		self.front = swap

	# 남쪽
	def move4(self,board,x,y):
		swap = self.down

		if board[x][y] == 0:
			board[x][y] = self.front
			self.down = self.front
		else:
			self.down = board[x][y]
			board[x][y] = 0
		
		self.front = self.up
		self.up = self.back
		self.back = swap

	def answer(self):
		print(str(self.up))

temp = input().split()
d=dice()
for move in temp:
	if move == '1' and board[x][y+1]!=-1:
		d.move1(board,x,y+1)
		y+=1
		d.answer()
	elif move == '2' and board[x][y-1]!=-1:
		d.move2(board,x,y-1)
		y-=1
		d.answer()
	elif move == '3' and board[x-1][y]!=-1:
		d.move3(board,x-1,y)
		x-=1
		d.answer()
	elif move == '4' and board[x+1][y]!=-1:
		d.move4(board,x+1,y)
		x+=1
		d.answer()