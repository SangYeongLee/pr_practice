import queue

def solution(n, edge):
	nei = [[] for i in range(n+1)]
	for i in edge:
		nei[i[0]].append(i[1])
		nei[i[1]].append(i[0])
	distance=[-1 for i in range(n)]
	q=queue.Queue()
	q.put(1)
	distance[0]=0

	dMax=0
	answer=0
	while True:
		temp =q.get()
		#print(temp)
		for i in nei[temp]:
			if distance[i-1]==-1:
				q.put(i)
				distance[i-1]=distance[temp-1]+1
				if dMax<distance[temp-1]+1:
					answer=1
					dMax=distance[temp-1]+1
				elif dMax==distance[temp-1]+1:
					answer+=1

		if q.qsize()==0: break

	return answer
e=[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(6,e))
