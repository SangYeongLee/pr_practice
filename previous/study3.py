def allAns(arr,depth):
	ret=[]
	if depth==1:
		for i in arr:
			ret.append(str(i))
		return ret
	else:
		for i in arr:
			temp = arr.copy()
			temp.remove(i)
			for j in allAns(temp,depth-1):
				val = str(i)+j
				if val not in ret:
					ret.append(val)
		return ret

def checkAns(a,t):
	strike=0
	ball=0
	ans=[]
	test=[]

	for i in range(len(a)):
		ans.append(a[i])
		test.append(t[i])

	#ball check
	for i in range(len(ans)):
		compare = test[i]
		temp = ans.copy()
		temp.pop(i)
		
		for j in temp:
			if compare==j:
				ball+=1
				break

	for i in range(len(ans)):
		if ans[i]==test[i]:
			strike+=1

	return strike,ball

def solution(baseball):
	numbers=[1,2,3,4,5,6,7,8,9]
	answer=0

	for ans in allAns(numbers,3):
		for trys in baseball:
			flag=1
			strike, ball = checkAns(ans,str(trys[0]))
			if strike!=trys[1] or ball!=trys[2]:
				flag=0
				break

		if flag==1: answer+=1

	return answer

print(solution([[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]))