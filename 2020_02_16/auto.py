def solution(words):
	answer = 0
	words = sorted(words)
	min_list = [0 for i in range(len(words))]
	for i in range(1,len(words)):
		j=0
		end=False
		while True:
			if words[i-1][j]!=words[i][j] : break
			if len(words[i-1])==j+1:
				end=True
				break
			j+=1
		
		if min_list[i-1]<j+1:
			min_list[i-1]=j+1

		if end: j+=1

		if min_list[i]<j+1:
			min_list[i]=j+1
		
		answer+=min_list[i-1]
	
	return answer+min_list[-1]

test = ["word","war","warrior","world"]
print(solution(test))