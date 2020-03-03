def cnt_digit(num):
	ret = 1
	while num//10!=0: 
		num = num//10
		ret+=1
	return ret

def solution(s):
	str_len = len(s)
	answer = str_len

	for l in range(1,str_len//2+1):
		cur=0
		i=0
		while True:
			if i+2*l > str_len: break
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
				
		cur+=str_len-i

		if answer>cur: answer = cur

	return answer

if __name__ == "__main__":
	test = "abababcdcdababcdcd"
	print(solution(test))