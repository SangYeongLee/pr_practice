import math

def solution(progress,speeds):
	answer=[]
	complete=[]
	for i in range(len(progress)):
		complete.append(math.ceil((100-progress[i])/speeds[i]))
	
	temp=[]
	for i in complete:
		if len(temp)==0 or temp[0]>=i:
			temp.append(i)
		else:
			answer.append(len(temp))
			temp=[i]
	answer.append(len(temp))
	return answer

print(solution([93,30,55],[1,30,5]))