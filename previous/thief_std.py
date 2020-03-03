def solution(money):
	answer=0

	cache1 = money[0]
	cache2 = 0
	for i in range(1,len(money)-1):
		if cache2<cache1:
			temp = cache2
			cache2 = cache1
			cache1 = temp+money[i]
		else:
			cache1=money[i]+cache2
	
	answer = max(cache1,cache2)
	cache1=0
	cache2=0
	for i in range(1,len(money)):
		if cache2<cache1:
			temp = cache2
			cache2 = cache1
			cache1 = temp+money[i]
		else:
			cache1=money[i]+cache2
	
	return max(answer,cache1,cache2)

print(solution([3,2,5,1,2,7,3]))