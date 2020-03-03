def solution(arrangement):
	answer=0
	bar=0
	for i in arrangement:
		if i==')':
			bar-=1
			if prev: 
				answer+=bar
				prev=False
			else: answer+=1
		else:
			bar+=1
			prev=True
	return answer

print(solution("()((())(()))"))