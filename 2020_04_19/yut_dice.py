#https://www.acmicpc.net/problem/17825
def move(start, m):
	set1 = [10, -13, -16, -19, -25, -30, -35, 40]
	set2 = [20, -22, -24, -25, -30, -35, 40]
	set3 = [30, -28, -27, -26, -25, -30, -35, 40]
	if start in set1:
		cur = set1.index(start)
		
		if cur+m >= len(set1): return 41
		return set1[cur+m]
	elif start in set2:
		cur = set2.index(start)

		if cur+m >= len(set2): return 41
		return set2[cur+m]
	elif start in set3:
		cur = set3.index(start)
		
		if cur+m >= len(set3): return 41
		return set3[cur+m]
	else:
		if start+2*m>40: return 41
		return start+2*m

lst = list(map(int, input().split()))

ans = 0
# [turn, 말 4개, 지금 turn까지 점수]
stack = [[0,0,0,0,0,0]]

while len(stack)!=0:
	cur = stack.pop()
	
	for i in range(1,5):
		temp = [j for j in cur]
		
		if temp[i]!=41:
			after = move(temp[i],lst[temp[0]])
			if after in temp[1:5] and after!=41:
				continue

			temp[i] = after
			if after != 41:
				temp[5]+=abs(temp[i]) 
		else:
			continue

		temp[0]+=1
		
		if temp[0]==10:
			if ans<temp[5]: ans = temp[5]
		else: 
			stack.append(temp)
	
print(ans)