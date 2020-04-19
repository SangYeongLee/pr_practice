tmp = input().split()
n, m, t = int(tmp[0]),int(tmp[1]),int(tmp[2])

plate = [[0 for i in range(m)] for j in range(n)]
for i in range(n):
	tmp = input().split()
	for j in range(len(tmp)):
		plate[i][j] = int(tmp[j])

for rotate in range(t):

	tmp = input().split()
	mult, direc, num = int(tmp[0]),int(tmp[1]),int(tmp[2])
	target = mult

	while target<=n:		
		if direc==0:
			swap = plate[target-1][m-num:] + plate[target-1][:m-num]

			plate[target-1] = swap
		else:
			swap = plate[target-1][num:] + plate[target-1][:num]
		
			plate[target-1] = swap

		target+=mult

	cnt = 0
	avg = 0
	d_set = set()
	for i in range(n):
		for j in range(m):
			if plate[i][j]==0: continue

			cnt+=1
			avg+=plate[i][j]
			if (i>0 and plate[i][j]==plate[i-1][j]) or (i<n-1 and plate[i][j]==plate[i+1][j]):
				d_set.add((i,j))
			elif plate[i][j] == plate[i][(j-1)%m] or plate[i][j] == plate[i][(j+1)%m]:
				d_set.add((i,j))

	if cnt==0:
		break

	avg = avg/cnt
	if len(d_set)==0:
		for i in range(n):
			for j in range(m):
				if plate[i][j]==0: continue

				if avg>plate[i][j]: plate[i][j]+=1
				elif avg<plate[i][j]: plate[i][j]-=1
	else:
		for idx in d_set:
			plate[idx[0]][idx[1]]=0

ans = 0
for row in plate:
	ans+=sum(row)
print(ans)