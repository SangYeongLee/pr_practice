def ceil(num):
	if num-int(num)>0: return int(num)+1
	return int(num)

N = int(input())

lst = [0 for i in range(N)]
temp = input().split()
for i in range(len(temp)):
	lst[i] = int(temp[i])

temp = input().split()
chief, sub = int(temp[0]),int(temp[1])

answer = 0
for cur in lst:
	#총감독관 감시 가능 인원 제외한 인원에 필요한 감독관 수
	if cur>chief:
		answer+=1+ceil((cur-chief)/sub)
	else:
		answer+=1

print(answer)