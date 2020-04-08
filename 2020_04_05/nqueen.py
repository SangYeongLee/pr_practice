#https://www.acmicpc.net/problem/9663
n = int(input())

stack = [(0,i) for i in range(n-1,-1,-1)]

queen_state = [-1 for i in range(n)]

ans=0
while len(stack)!=0:
	cur = stack.pop()
	if cur[0]==n-1:
		ans+=1
		continue

	queen_state[cur[0]] = cur[1]

	for i in range(n-1,-1,-1): #그 row에 스택에 넣을게 있는지 (cur[0]+1,i)
		node = (cur[0]+1,i)
		flag = True
		for j in range(cur[0]+1): 
			prev = (j,queen_state[j])
			# 앞에 queen_state 에 들어가있는거랑 다 비교 (j,queen_state[j])
			if prev[1]==node[1] or abs(prev[0]-node[0])==abs(prev[1]-node[1]):
				flag = False
				break
		
		if flag:
			stack.append(node)
	
print(ans)