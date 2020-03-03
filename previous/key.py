import copy

# M*M 사이즈 key를 회전해서 만든 4가지 key 배열을 반환
def rotate(key):
	ret=[]
	m=len(key)
	for i in range(4):
		temp = [[0 for i in range(m)] for j in range(m)]
		for i in range(m):
			for j in range(m):
				temp[m-j-1][i]=key[i][j]
		key = temp
		ret.append(temp)

	return ret

# 열리는지 확인하는 함수 
#(zero padding map, key list, start index1, start index2, key size, lock size)
def isUnLock(lock_map,keys,i,j,key_size,lock_size):
	#zero padding map에서 lock부분의 시작과 끝 인덱스
	lock_start = key_size-1
	lock_end = lock_size+key_size-2
	
	#4가지 key에 대해서 시작 인덱스에서 key와 lock 값을 더한 map만듬
	for key in keys:
		temp = copy.deepcopy(lock_map)
		for x in range(i,i+key_size):
			for y in range(j,j+key_size):
				if x>=lock_start and x<=lock_end and y>=lock_start and y<=lock_end:
					temp[x][y] += key[x-i][y-j]

		#lock 영역이 모두 1인지 체크
		flag=True
		for x in range(lock_start,lock_end+1):
			for y in range(lock_start,lock_end+1):
				if temp[x][y] != 1:
					flag=False
					break
			if not flag: break

		if flag: return True

	return False

def solution(key, lock):
	answer = False
	m = len(key)
	n = len(lock)
	#zero padding
	lock_map = [[0 for i in range(n+m*2-2)] for j in range(n+m*2-2)]
	for i in range(m-1,n+m-1):
		for j in range(m-1,n+m-1):
			lock_map[i][j] = lock[i-m+1][j-m+1]
	
	#모든 영역돌면서 체크
	keyList = rotate(key)
	for i in range(n+m-1):
		for j in range(n+m-1):
			if isUnLock(lock_map,keyList,i,j,m,n): return True

	return answer

if __name__=="__main__":
	key = [	[0, 1, 0], 
			[1, 1, 1], 
			[0, 0, 1]]
	lock = [	[1, 1, 1, 1], 
				[1, 1, 1, 1], 
				[1, 1, 1, 1], 
				[1, 1, 0, 1]]
	print(solution(key,lock))