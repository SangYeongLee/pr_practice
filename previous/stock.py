def solution(prices):
	answer = [0 for i in range(len(prices))]
	stack = [(prices[0],0)]
	for i in range(1,len(prices)):
		if stack[-1][0]<=prices[i]:
			stack.append((prices[i],i))
		else:
			while len(stack)!=0 and stack[-1][0]>prices[i]:
				temp = stack.pop()
				answer[temp[1]]=i-temp[1]
			stack.append((prices[i],i))

	temp = stack.pop()
	for i in stack:
		answer[i[1]]=temp[1]-i[1]
	return answer

print(solution([4,4,6,5,5,2]))