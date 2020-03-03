def solution(weight):
	weight.sort()
	upperBound = 0
	for i in weight:
		if upperBound+1 < i: return upperBound+1
		upperBound+=i
	
	return upperBound+1

print(solution([3, 1, 6, 2, 7, 1]))