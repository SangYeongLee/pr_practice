#https://www.acmicpc.net/problem/17471

from itertools import combinations

#리스트의 노드들이 연결되어 있는지 체크
def chk_connected(lst):
	global matrix
	n=len(lst)
	if n==1:
		return True
	else:
		stack = [lst[0]] #dfs로 체크
		visited = [lst[0]]
		while len(stack)>0:
			cur = stack.pop()

			for i in range(len(matrix)):
				#리스트에 있으면서 연결된 노드만 스택에 넣음
				if matrix[cur][i]==1 and i in lst and i not in visited:
					stack.append(i)
					visited.append(i)

		#방문 노드가 리스트 길이랑 같으면 연결된 상태
		if len(visited)!=n:
			return False
		else:
			return True

#두 그룹으로 나누기
def divide(lst):
	ret = []
	for n in range(1,len(lst)//2+1):
		for comb in list(combinations(lst,n)):
			set2 = []
			for i in lst:
				if i not in comb: set2.append(i)
			ret.append([comb,set2])
	return ret

n = int(input())
lst = [i for i in range(n)]

nums = list(map(int,input().split()))
matrix = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
	temp = input().split()
	for j in range(int(temp[0])):
		matrix[i][int(temp[j+1])-1] = 1

ans = 1000
for d_case in divide(lst):
	#두 그룹 다 연결되잇으면 차이 계산
	if chk_connected(d_case[0]) and chk_connected(d_case[1]):
		val = 0
		for i in range(n):
			if i in d_case[0]:
				val+=nums[i]
			else:
				val-=nums[i]
		ans = min(abs(val),ans)
if ans==1000: 
	print(-1)
else:
	print(ans)