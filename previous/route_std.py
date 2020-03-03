def solution(m, n, puddles):
	cache = [[0 for i in range(m)] for j in range(n)]
	for water in puddles:
		cache[water[1]-1][water[0]-1] = -1
	cache[n-1][m-1]=1
	return numRoute(0,0,cache)%1000000007

def numRoute(m,n,cache):
	if cache[n][m]>0: return cache[n][m]
	if cache[n][m]<0: return 0
	
	ret=0
	if n+1<len(cache):
		if cache[n+1][m]>0: ret+=cache[n+1][m]
		else: ret+=numRoute(m,n+1,cache)
	if m+1<len(cache[0]):
		if cache[n][m+1]>0: ret+=cache[n][m+1]
		else: ret+=numRoute(m+1,n,cache)
	cache[n][m]= ret


	return ret

print(solution(4,3,[[2,2],[1,2],[3,2]]))