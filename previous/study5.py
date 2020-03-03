def solution(n, lost, reserve):
	student = [1 for i in range(n)]
	for i in range(n):
		if i+1 in lost:
			student[i]-=1
		if i+1 in reserve:
			student[i]+=1

	answer=0
	for i in range(n):
		if i==0:
			if student[i]==2 and student[i+1]==0:
				student[i]-=1 
				student[i+1]+=1
		else:
			if student[i]==2:
				if student[i-1]==0:
					student[i-1]+=1
					student[i]-=1
				elif i+1<n:
					if student[i+1]==0:
						student[i+1]+=1
						student[i]-=1

	for i in student:
		if i!=0: answer+=1

	return answer

print(solution(20,[1,2,4,5],[5]))