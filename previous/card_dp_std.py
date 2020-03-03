def solution(left,right):
	answer=0
	cache = [[-1 for i in range(len(left)+1)] for j in range(len(right)+1)]
	cache[0][0]=0
	for i in range(len(left)):
		for j in range(len(right)):
			if cache[i][j]!=-1:
				if left[i] > right[j] and cache[i][j+1]<cache[i][j]+right[j]:
					cache[i][j+1]=cache[i][j]+right[j]
				if cache[i+1][j+1]<cache[i][j]:
					cache[i+1][j+1]=cache[i][j]
				if cache[i+1][j]<cache[i][j]:
					cache[i+1][j] = cache[i][j]
	for i in range(len(left)):
		if cache[i][len(right)]>answer:
			answer=cache[i][len(right)]
		if cache[len(left)][i]>answer:
			answer=cache[len(left)][i]

	return answer

print(solution([3,2,5],[2,4,1]))