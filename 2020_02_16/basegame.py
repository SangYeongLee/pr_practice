#10진수를 2~16진수로 변환하는 함수
def baseConv(n,num):
	if num==0:return "0"
	t="0123456789ABCDEF"
	ret=""
	while num>0:
		ret+=t[int(num%n)]
		num=int(num/n)

	return ret[::-1]

def solution(n,t,m,p):
	answer = ""
	num=0
	i=0	#턴 계산하는 변수

	while True:
		cur = baseConv(n,num)

		#0부터 시작해서 플레이어 턴마다 리스트에 넣어줌
		for ch in cur:
			if i%m==p-1: 
				answer+=ch
				t-=1
			if t==0: return answer
			i+=1
		num+=1

print(solution(2,4,2,1))