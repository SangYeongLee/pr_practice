def fibo(N,cache):
	if N<2: 
		cache[N]=1
		return 1
	if cache[N]!=-1: return cache[N]
	cache[N] = fibo(N-1,cache)+fibo(N-2,cache)
	return cache[N]

def solution(N):
    answer = 0
    cache = [-1 for i in range(N)]
    ret = 2*(fibo(N-1,cache)*2+fibo(N-2,cache))
    return ret

print(solution(6))