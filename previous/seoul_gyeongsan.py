def solution(K, travel):
	cache = [[travel[0][0],travel[0][1]],[travel[0][2],travel[0][3]]]
	i=1
	answer=0

	for travel_e in travel[1:]:
		i+=1
		j=0
		temp = [[0,0] for j in range(2**i)]
		for cache_e in cache:
			if cache_e[0]==0: break

			if cache_e[0]+travel_e[0]<=K:
				temp[j] = [cache_e[0]+travel_e[0],cache_e[1]+travel_e[1]]
				j+=1
			if cache_e[0]+travel_e[2]<=K:
				temp[j] = [cache_e[0]+travel_e[2],cache_e[1]+travel_e[3]]
				j+=1

		cache = temp

	for i in cache:
		if answer<i[1]: answer = i[1]

	return answer

t=[[500, 200, 200, 100], [800, 370, 300, 120], [700, 250, 300, 90]]
print(solution(100, [[1, 1, 1, 1], [98, 1000, 1, 1], [1, 1, 1, 1]]))