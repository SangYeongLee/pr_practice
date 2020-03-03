def diffCalc(letter):
	diff = ord(letter)-ord('A')
	if diff <= 13:
		return diff
	else:
		return 26-diff

def retNear(current,arr):
	if arr[current]!='A': return 0
	for i in range(1,int(len(arr)/2)+1):
		if arr[(current+i)%len(arr)]!='A':
			return (current+i)%len(arr)
		elif arr[(current-i)%len(arr)]!='A':
			return (current-i)%len(arr)
	return -1

def solution(name):
	answer = 0
	idx=0
	while retNear(idx,name)!=-1:
		i=retNear(idx,name)
		answer+=min(abs(i-idx),idx+len(name)-i)+diffCalc(name[i])
		idx=i
		name=name[0:i]+'A'+name[i+1:]
		
	return answer

print(solution("AAAAABAZAA"))