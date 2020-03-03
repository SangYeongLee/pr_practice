def calc_diff(w1,w2):
	ret=0
	for i in range(len(w1)):
		if w1[i]!=w2[i]: ret+=1
	return ret

def solution(begin, target, words):
	stack=[-1]
	convert_num=[100 for i in range(len(words)+1)]
	convert_num[0]=0

	while True:
		temp = stack.pop()
		if temp==-1: top = begin
		else: top = words[temp]
		
		for i in range(len(words)):
			if calc_diff(words[i],top)==1 and convert_num[i+1]>convert_num[temp+1]:
				stack.append(i)
				convert_num[i+1]=convert_num[temp+1]+1

		if len(stack)==0: break
	for i in range(len(words)):
		if target==words[i] and convert_num[i+1]!=100: return convert_num[i+1]

	return 0


print(solution("hit","cog",["sot","dot","lot","dog","cog"]))