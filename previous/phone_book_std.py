def solution(phone_book):
	temp=sorted(phone_book)
	for i in range(len(temp)-1):
		if temp[i]==temp[i+1][:len(temp[i])]: return False
	return True

a=["3312","117","119","123123123","11722223445"]
print(solution(a))
