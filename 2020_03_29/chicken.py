#https://www.acmicpc.net/problem/15686

from itertools import combinations
import sys

temp = input().split()
n, m = int(temp[0]), int(temp[1])

board = []
for i in range(n):
	board.append(list(map(int, input().split())))

chicken = []
home = []
for i in range(n):
	for j in range(n):
		if board[i][j] == 1:
			home.append((i,j))
		elif board[i][j] == 2:
			chicken.append((i,j))

ch_dis = []
for cur in home:
	temp = []
	for ch in chicken:
		temp.append(abs(ch[0]-cur[0])+abs(ch[1]-cur[1]))
	ch_dis.append(temp)

idx = [ i for i in range(13)]

ans = sys.maxsize
for comb in list(combinations(idx[:len(chicken)],m)):
	temp = 0
	for dis in ch_dis:
		min_val = sys.maxsize
		for i in comb:
			if min_val>dis[i]:
				min_val = dis[i]
		temp+=min_val

	if ans > temp:
		ans = temp

print(ans)