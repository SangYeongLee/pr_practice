def solution(n, results):
	answer = 0
	win = [set() for i in range(n)]
	lose = [set() for i in range(n)]
	

	for i in range(1,n+1):
		for temp in results:
			if temp[0]==i: win[i-1].add(temp[1])
			if temp[1]==i: lose[i-1].add(temp[0])

		for temp in win[i-1]:
			lose[temp-1].update(lose[i-1])
		for temp in lose[i-1]:
			win[temp-1].update(win[i-1])

	for i in range(n):
		if len(win[i])+len(lose[i])==n-1:
			answer+=1
			
	return answer

print(solution(5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
