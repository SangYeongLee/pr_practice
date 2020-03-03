def solution(n, computers):
	ret = 0
	stack=[]

	while True:
		for i in range(n):
			if computers[i][i]==1:
				stack.append(i)
				break

		if len(stack)==0:break

		while True:
			temp = stack.pop()
			for i in range(n):
				if computers[temp][i]==1:
					if temp!=i: stack.append(i)
					computers[temp][i]=0
					computers[i][temp]=0

			if len(stack)==0:
				ret+=1
				break

	return ret
	

print(solution(4,[[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1], [0, 0, 1, 1]]))