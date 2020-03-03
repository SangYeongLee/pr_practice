from collections import deque

def solution(bridge_length, weight, truck_weights):
	answer=0
	onWeight=0
	trucks = deque(truck_weights)
	onBridge = deque([])

	while len(trucks)+len(onBridge)!=0:
		answer+=1
		for i in onBridge:
			i[1]+=1

		if len(onBridge)!=0 and onBridge[0][1]==bridge_length:
			temp = onBridge.popleft()
			onWeight-=temp[0]
		
		if len(trucks)!=0 and trucks[0]+onWeight<=weight:
			temp = trucks.popleft()
			onBridge.append([temp,0])
			onWeight+=temp
		
	return answer
print(solution(2,10,[7,4,5,6]))