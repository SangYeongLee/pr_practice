def solution(dartResult):
	answer = 0
	cur=0
	prev=0

	for i in range(len(dartResult)):
		if dartResult[i]>='0' and dartResult[i]<='9':
			if dartResult[i]=='0' and cur==1: 
				cur=10
				continue
			answer+=prev
			prev=cur
			cur=int(dartResult[i]);
		else:
			if dartResult[i]=='D':
				cur=cur**2
			elif dartResult[i]=='T':
				cur=cur**3
			elif dartResult[i]=='*':
				cur=cur*2
				prev=prev*2
			elif dartResult[i]=='#':
				cur=-cur

	answer+=prev+cur

	return answer

print(solution("10S2D*3T"))