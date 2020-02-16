def solution(msg):
	answer = []
	#딕셔너리 초기값
	dic={}
	for i in range(26):
		dic[chr(ord('A')+i)]=i+1

	i=0
	while i<len(msg):
		j=i
		#딕셔너리에 매칭되는 key가 없을 때까지
		while msg[i:j+1] in dic.keys() and j<len(msg):
			j+=1
		if j==len(msg): break
		#매칭된 문자열은 출력, 매칭 안된 문자열은 딕셔너리에 저장
		answer.append(dic[msg[i:j]])
		dic[msg[i:j+1]]=len(dic)+1
		i=j
	
	answer.append(dic[msg[i:j]])
	return answer

print(solution("KAKAOO"))