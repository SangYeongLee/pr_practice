import copy

def solution(tickets):
	answer = []
	stack = [("ICN",[])]

	while True:
		#print("stack:: "+str(stack))
		temp = stack.pop()
		push_list = []
	
		for i in range(len(tickets)):
			if tickets[i][0]==temp[0] and not i in temp[1]:
				path = copy.deepcopy(temp[1])
				path.append(i)
				push_list.append((tickets[i][1],path))

		push_list.sort(reverse=True)
		for i in range(len(push_list)):
			if len(push_list[i][1])==len(tickets):
				for j in push_list[i][1]:
					answer.append(tickets[j][0])
				answer.append(tickets[j][1])
				return answer
			stack.append(push_list[i])

	
print(solution([["ICN","SFO"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "AAA"], ["SFO", "AAA"], ["ATL", "ICN"], ["BBB","SFO"], ["SFO","BBB"],["AAA","SFO"]]))
print(solution([["ICN", "AAA"], ["ICN", "AAA"], ["ICN", "AAA"], ["AAA","AAB"], ["AAA", "AAD"], ["AAD", "ICN"], ["AAA", "AAC"], ["AAC", "ICN"]]))
print(solution([["ICN", "AAB"], ["ICN", "AAA"], ["AAA", "ICN"], ["AAB", "ICN"], ["AAA", "AAB"], ["AAB", "AAA"]]))