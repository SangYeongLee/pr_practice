f = open("input3.txt", 'r')
size = int(f.readline())
matrix = [[-1 for i in range(size)] for i in range(size)]
cache = [[-1 for i in range(size)] for i in range(size)]

for i in range(size):
	buff = f.readline().split()
	for j in range(i+1):
		matrix[i][j] = int(buff[j])

def path(i,j):
	global size
	global matrix,cache

	if i==size-1 : return matrix[i][j]
	if not cache[i][j] == -1 : return cache[i][j]
	
	print(str(i)+","+str(j))
	cache[i][j] = max(matrix[i][j]+path(i+1,j),matrix[i][j]+path(i+1,j+1))

	return max(matrix[i][j]+path(i+1,j),matrix[i][j]+path(i+1,j+1))

print(path(0,0))

f.close()
