def solution(number, k):
	answer = ""

	start=0
	for i in range(len(number)-k,0,-1):
		#남은 substring의 길이가 남은 결과 길이랑 같을때 -->1번
		if start+i==len(number): break
		maxVal=number[start]

		for j in range(start+1,len(number)-i+1):
			#최대값이 9일때 더 안돌고 바로 최대값 인덱스 표시하고 나감
			if maxVal=='9': break
			#최대값찾아서 인덱스표시
			if maxVal<number[j]: 
				start=j
				maxVal=number[j]
		#최대값 다음 인덱스 표시하고 결과 문자열에 붙임
		answer+=number[start]
		start+=1
	#1번 경우로 break되서 나올때 남은 substring 뒤에 붙이기
	if(i!=1): answer+=number[len(number)-i:]

	return answer

print(solution("9999999",3))
