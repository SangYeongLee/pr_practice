#https://www.acmicpc.net/problem/14891

#톱니바퀴 객체
class Gear:
	def __init__(self, pol):
		self.arg = []
		for i in pol:
			self.arg.append(int(i))
	#시계 방향
	def clock(self):
		swap = self.arg[7]
		for i in range(7,0,-1):
			self.arg[i] = self.arg[i-1]
		self.arg[0] = swap

	#반시계 방향
	def counter(self):
		swap = self.arg[0]
		for i in range(7):
			self.arg[i] = self.arg[i+1]
		self.arg[7] = swap

	#바퀴 상태 반환
	def ret(self):
		return self.arg

if __name__ == "__main__":
	#입력
	ans = 0
	gears = []
	for i in range(4):
		temp = Gear(input())
		gears.append(temp)

	k = int(input())
	for i in range(k):
		temp = input().split()
		n, direc = int(temp[0])-1, int(temp[1])
		
		#돌릴 바퀴들 저장하는 list (번호, 방향)
		target = [(n,direc)]

		cur = -direc
		#왼쪽으로 가면서 맞닿은 부분 비교해서 돌리는지 결정
		if n>0:
			t = n
			while t>0:
				if gears[t].ret()[6] != gears[t-1].ret()[2]:
					target.append((t-1,cur))
					cur = -cur
					t-=1
				else:
					break
		cur = -direc
		
		#오른쪽으로 가면서 맞닿은 부분 비교해서 돌리는지 결정
		if n<3:
			t = n
			while t<3:
				if gears[t+1].ret()[6] != gears[t].ret()[2]:
					target.append((t+1,cur))
					cur = -cur
					t+=1
				else:
					break

		#target에 있는 바퀴들 다 돌림
		for cur in target:
			if cur[1] == 1:
				gears[cur[0]].clock()
			else:
				gears[cur[0]].counter()

	#합
	val = 1
	for i in range(4):
		ans+=val*gears[i].ret()[0]
		val*=2

	print(ans)