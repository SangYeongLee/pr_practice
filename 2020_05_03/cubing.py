class Cube():
	def __init__(self):
		self.up = [['w','w','w'],['w','w','w'],['w','w','w']]
		self.down = [['y','y','y'],['y','y','y'],['y','y','y']]
		self.front = [['r','r','r'],['r','r','r'],['r','r','r']]
		self.back = [['o','o','o'],['o','o','o'],['o','o','o']]
		self.left = [['g','g','g'],['g','g','g'],['g','g','g']]
		self.right = [['b','b','b'],['b','b','b'],['b','b','b']]

	def t_front_clock(self):
		temp = [[self.front[i][j] for i in range(2,-1,-1)] for j in range(3)]
		self.front = temp

		temp = [self.up[2][i] for i in range(3)]
		for i in range(3):
			self.up[2][i] = self.left[2-i][2]
		for i in range(3):
			self.left[i][2] = self.down[0][i]
		for i in range(3):
			self.down[0][i] = self.right[2-i][0]
		for i in range(3):
			self.right[i][0] = temp[i]

	def t_front_un(self):
		for i in range(3):
			self.t_front_clock()

	def t_back_clock(self):
		temp = [[self.back[i][j] for i in range(2,-1,-1)] for j in range(3)]
		self.back = temp

		temp = [self.up[0][i] for i in range(3)]
		for i in range(3):
			self.up[0][i] = self.right[i][2]
		for i in range(3):
			self.right[i][2] = self.down[2][2-i]
		for i in range(3):
			self.down[2][i] = self.left[i][0]
		for i in range(3):
			self.left[i][0] = temp[2-i]

	def t_back_un(self):
		for i in range(3):
			self.t_back_clock()

	def t_right_clock(self):
		temp = [[self.right[i][j] for i in range(2,-1,-1)] for j in range(3)]
		self.right = temp

		temp = [self.up[i][2] for i in range(3)]
		for i in range(3):
			self.up[i][2] = self.front[i][2]
		for i in range(3):
			self.front[i][2] = self.down[i][2]
		for i in range(3):
			self.down[i][2] = self.back[2-i][0]
		for i in range(3):
			self.back[i][0] = temp[2-i]

	def t_right_un(self):
		for i in range(3):
			self.t_right_clock()

	def t_left_clock(self):
		temp = [[self.left[i][j] for i in range(2,-1,-1)] for j in range(3)]
		self.left = temp

		temp = [self.up[i][0] for i in range(3)]
		for i in range(3):
			self.up[i][0] = self.back[2-i][2]
		for i in range(3):
			self.back[i][2] = self.down[2-i][0]
		for i in range(3):
			self.down[i][0] = self.front[i][0]
		for i in range(3):
			self.front[i][0] = temp[i]

	def t_left_un(self):
		for i in range(3):
			self.t_left_clock()

	def t_up_clock(self):
		temp = [[self.up[i][j] for i in range(2,-1,-1)] for j in range(3)]
		self.up = temp

		temp = [self.front[0][i] for i in range(3)]
		for i in range(3):
			self.front[0][i] = self.right[0][i]
		for i in range(3):
			self.right[0][i] = self.back[0][i]
		for i in range(3):
			self.back[0][i] = self.left[0][i]
		for i in range(3):
			self.left[0][i] = temp[i]

	def t_up_un(self):
		for i in range(3):
			self.t_up_clock()

	def t_down_clock(self):
		temp = [[self.down[i][j] for i in range(2,-1,-1)] for j in range(3)]
		self.down = temp

		temp = [self.front[2][i] for i in range(3)]
		for i in range(3):
			self.front[2][i] = self.left[2][i]
		for i in range(3):
			self.left[2][i] = self.back[2][i]
		for i in range(3):
			self.back[2][i] = self.right[2][i]
		for i in range(3):
			self.right[2][i] = temp[i]

	def t_down_un(self):
		for i in range(3):
			self.t_down_clock()

	def printCube(self):
		for row in self.up:
			for i in row:
				print(i,end='')
			print()

	def printAll(self):
		for i in range(3):
			print("\t\t",self.up[i])
		for i in range(3):
			print(self.left[i],"",self.front[i],self.right[i],self.back[i])
		for i in range(3):
			print("\t\t",self.down[i])
		print()

n = int(input())
for i in range(n):
	cube = Cube()
	t = int(input())
	
	t_info = input().split()
	
	for j in range(t):
		side = t_info[j][0]
		direc = t_info[j][1]

		if side == 'L':
			if direc=='+':
				cube.t_left_clock()
			else:
				cube.t_left_un()
		elif side == 'R':
			if direc=='+':
				cube.t_right_clock()
			else:
				cube.t_right_un()
		elif side == 'F':
			if direc=='+':
				cube.t_front_clock()
			else:
				cube.t_front_un()
		elif side == 'B':
			if direc=='+':
				cube.t_back_clock()
			else:
				cube.t_back_un()
		elif side == 'U':
			if direc=='+':
				cube.t_up_clock()
			else:
				cube.t_up_un()
		else:
			if direc=='+':
				cube.t_down_clock()
			else:
				cube.t_down_un()
	
	cube.printCube()