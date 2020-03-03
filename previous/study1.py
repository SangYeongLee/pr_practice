def solution(answers):
	p1 = [1,2,3,4,5]
	p2 = [2,1,2,3,2,4,2,5]
	p3 = [3,3,1,1,2,2,4,4,5,5]
    
	answer = [0,0,0]
	for i in range(len(answers)):
		if p1[i%5]==answers[i]: answer[0]+=1
		if p2[i%8]==answers[i]: answer[1]+=1
		if p3[i%10]==answers[i]: answer[2]+=1

	ret=[1]
	maxval = answer[0]
	for i in range(1,3):
		if maxval == answer[i]:
			ret.append(i+1)
		elif maxval<answer[i]:
			maxval=answer[i]
			ret=[]
			ret.append(i+1)

	return ret


test=[1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,2,4,4,5,5]
t2=[1,3,2,4,2,4,4]
print(solution(test))
print(solution(t2))