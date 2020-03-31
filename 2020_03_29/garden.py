#https://www.acmicpc.net/problem/18809

from itertools import combinations
from collections import deque

temp = list(map(int, input().split()))
n,m,r,g = temp[0], temp[1], temp[2], temp[3]

garden = [[0 for i in range(m+2)] for j in range(n+2)]
garden_time = [[0 for i in range(m+2)] for j in range(n+2)]
spot = []

for i in range(n):
	temp = input().split()
	for j in range(m):
		garden[i+1][j+1] = int(temp[j])
		if garden[i+1][j+1] == 2:
			spot.append((i+1,j+1))

idx = [i for i in range(len(spot))]
near = [(0,1),(1,0),(0,-1),(-1,0)]

ans = 0
# 3: 빨강 , 4: 녹색, 5: 꽃
for brute in list(combinations(idx,r+g)):
	for red in list(combinations(brute,r)):
		val = 0
		temp = [garden[i][:] for i in range(len(garden))]
		time_temp = [garden_time[i][:] for i in range(len(garden))]
		
		q = deque()
		for i in brute:
			if i in red:
				q.append([spot[i],1])
				temp[spot[i][0]][spot[i][1]] = 3
			else:
				q.append([spot[i],1])
				temp[spot[i][0]][spot[i][1]] = 4
		
		while len(q)!=0:
			cur = q.popleft()
			
			x, y = cur[0][0], cur[0][1]
			t = cur[1]
			
			for f in near:
				if (temp[x+f[0]][y+f[1]]==1 or temp[x+f[0]][y+f[1]]==2) and temp[x][y]!=5:
					temp[x+f[0]][y+f[1]] = temp[x][y]
					time_temp[x+f[0]][y+f[1]] = t
					q.append([(x+f[0],y+f[1]),t+1])
				elif ((temp[x+f[0]][y+f[1]]==3 and temp[x][y]==4) or (temp[x+f[0]][y+f[1]]==4 and temp[x][y]==3)) and time_temp[x+f[0]][y+f[1]]==t:
					temp[x+f[0]][y+f[1]] = 5
					val+=1
			
		if ans<val:
			ans = val
	
print(ans)