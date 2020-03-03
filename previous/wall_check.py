# num을 cnt만큼 분할하는 함수
def partition(num, cnt):
	if cnt==1: return [[num]]
	else:
		ret=[]
		for i in range(1,num-cnt+2):
			for j in partition(num-i,cnt-1):
				temp=[i]+j
				ret.append(temp)
		return ret

#같은 분할인지 체크
def same_list(lst):
	ret=[]
	size = len(lst)
	for start in range(size):
		temp = lst[start:size]
		temp+=lst[:start]
		ret.append(temp)
	return ret

#리스트 안의 취약지점을 모두 체크하는 데 걸리는 시간
def calc_dis(lst,n):
	ret=[]
	for cur in lst:
		temp=0
		for i in range(len(cur)-1):
			if cur[i]>cur[i+1]:
				temp+=n-cur[i]+cur[i+1]
			else:
				temp+=cur[i+1]-cur[i]
		ret.append(temp)
	return ret

def solution(n, weak, dist):
	answer = 0
	dist = sorted(dist,reverse=True)

	for i in range(len(dist)):
		#가장 긴 범위를 체크하는 친구들
		member = dist[:i+1]

		#분할
		prev = partition(len(weak),i+1)
		part_list=[]

		#중복된 분할 제거
		while len(prev)!=0:
			cur = prev.pop()
			lst=same_list(cur)
			for idx,val in enumerate(prev):
				if val in lst: del(prev[idx])
			part_list.append(cur)

		#분할 별로 시작 위치 바꿔가면서 체크 거리 계산
		for part in part_list:
			for idx in range(len(weak)):
				weak_partition = []
				cnt=0
				for cur in part:
					temp = []
					for j in range(cur):
						temp.append(weak[(idx+cnt)%len(weak)])
						cnt+=1
					weak_partition.append(temp)
				
				#체크거리를 정렬해서 모두 체크할 수 있는지 dist랑 비교
				dis_list = sorted(calc_dis(weak_partition,n),reverse=True)
				flag=True
				for j in range(len(dis_list)):
					if member[j]<dis_list[j]:
						flag=False
						break

				#가능하면 반환
				if flag:
					return i+1
	return -1

if __name__ == "__main__":
	weak = [1, 5, 10, 16, 22, 25]	
	dist =  [3, 4, 6]
	print(solution( 12, [0,4,8], [4,3]))
	print(partition(6,3))