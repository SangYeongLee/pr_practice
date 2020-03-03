def solution(people, limit):
	answer = 0
	people.sort()

	minP=0
	maxP=len(people)-1
	while maxP>=minP:
		if people[maxP]+people[minP]<=limit:
			answer+=1
			minP+=1
			maxP-=1
		else:
			answer+=1
			maxP-=1
	
	return answer
print(solution([40,60,60,70,80,90],100))