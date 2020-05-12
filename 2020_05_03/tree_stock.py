temp = input().split()
n, m, k = int(temp[0]),int(temp[1]),int(temp[2])

ground = [[5 for i in range(n)] for j in range(n)]
tree = dict()
for i in range(n):
	for j in range(n):
		tree[(i,j)]=[]
board = []
near = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,1),(1,-1),(-1,-1)]

for i in range(n):
	board.append(list(map(int,input().split())))

for i in range(m):
	temp = input().split()
	tree[(int(temp[0])-1,int(temp[1])-1)].append(int(temp[2]))

for year in range(k):
	#spring , summer
	for idx in tree:
		#같은 칸의 나무
		for i in range(len(tree[idx])-1,-1,-1):
			if ground[idx[0]][idx[1]]<tree[idx][i]:
				for cur in tree[idx][:i+1]:
					ground[idx[0]][idx[1]]+=cur//2
				#ground[idx[0]][idx[1]] += sum(tree[idx][:i+1])//2
				tree[idx] = tree[idx][i+1:]
				break
			else:
				ground[idx[0]][idx[1]]-=tree[idx][i]
				tree[idx][i]+=1

	#fall
	for idx in tree:
		cnt=0
		for cur in tree[idx]:
			if cur%5==0:
				cnt+=1
			elif cur<5:
				break

		if cnt>0:
			for i in near:
				if 0<=idx[0]+i[0]<=n-1 and 0<=idx[1]+i[1]<=n-1:
					tree[(idx[0]+i[0],idx[1]+i[1])]+=[1 for j in range(cnt)]
	#winter
	for i in range(n):
		for j in range(n):
			ground[i][j]+=board[i][j]

ans = 0
for i in tree:
	ans+=len(tree[i])
print(ans)