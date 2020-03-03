def cnt_digit(num):
	ret = 1
	while num//10!=0: 
		num = num//10
		ret+=1
	return ret

def solution(s):
	str_len = len(s)
	answer = str_len
	iter_idx=[]
	#돌면서 첫 글자랑 같은거 찾기, 문자열의 절반 넘어가서 위치하는 애는 필요없으니까 뺌
	for idx, val in enumerate(s[1:],start=1):
		if val == s[0] and idx-1<str_len//2:
			iter_idx.append(idx)
	
	#첫 글자랑 같은거 없으면 걍 길이 반환
	if len(iter_idx)==0: return str_len

	for l in iter_idx:
		cur=0
		i=0
		while True:
			#범위 안넘는지
			if i+2*l > str_len: break
			'''
			같은 문자열인지 비교해서 같으면 그거랑 같은 거 개수세서
			(숫자 길이)+(반복 문자열 길이) ex>10aaa면 2+3
			같은 문자열아니면 그게 처음이면 못 줄이는거니까 패스
			나머지는 글자수 1늘리고 다음걸로 이동
			'''
			if s[i:i+l] == s[i+l:i+2*l]:
				cnt=1
				while s[i:i+l] == s[i+l:i+2*l]:
					cnt+=1
					i=i+l
				cur+=l+cnt_digit(cnt)
				i = i+l
			else:
				cur+=l
				i+=l

		#나머지 글자 붙여줌
		cur+=str_len-i

		if answer>cur: answer = cur
		#print("answer "+str(answer))

	return answer

if __name__ == "__main__":
	test = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
	print(solution(test))