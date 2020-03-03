board = [[0 for col in range(100)] for row in range(100)]
cache = [[-1 for col in range(100)] for row in range(100)]

def jump(j, i, size):
	global board
	global cache
	if j >= size or i >= size: return False
	if board[j][i] == -1 : return True
	if cache[j][i] != -1 : return cache[j][i]
	jmp_size = board[j][i]
	cache[j][i] = (jump(j+jmp_size,i,size) or jump(j,i+jmp_size,size))
	return cache[j][i]

f = open("input.txt", 'r')

#입출력
i=0
while True:
	j=0
	line = f.readline()
	if not line: break
	buff= line.split()
	#print(buff , len(buff))
	for j in range(len(buff)):
		board[i][j] = int(buff[j])
	i+=1
board_size = i

print(jump(0,0,board_size))
for i in range(7):
	print('')
	for j in range(7):
		print(board[j][i],end=' ')

for i in range(7):
	print('')
	for j in range(7):
		print(cache[j][i],end=' ')

f.close()