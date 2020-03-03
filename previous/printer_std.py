import queue
def solution(priorities, location):
	answer=0
	print_q = queue.Queue()
	pri_sort = sorted(priorities,reverse=True)
	for i in range(len(priorities)):
		print_q.put((i,priorities[i]))
	
	while True:
		if print_q.qsize()==0: break
		
		temp = print_q.get()
		if temp[1]==pri_sort[answer]:
			answer+=1
			if temp[0]==location: break
		else:
			print_q.put(temp)
		
	return answer

print(solution([1, 1, 9, 1, 1, 1, 5],3))