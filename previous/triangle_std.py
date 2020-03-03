cache = [[-1 for i in range(j)] for j in range(1,501)]

def maxSum(triangle,height,n,leaf):
	global cache
	if cache[height][n]!=-1: return cache[height][n]
	if height==leaf: 
		cache[height][n]=triangle[height][n]
		return cache[height][n]

	cache[height][n] = max(triangle[height][n]+maxSum(triangle,height+1,n,leaf),triangle[height][n]+maxSum(triangle,height+1,n+1,leaf))
	return cache[height][n]


def solution(triangle):
    n=len(triangle)
    return maxSum(triangle,0,0,n-1)

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
print(cache[:7])