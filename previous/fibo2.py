cache={0:0, 1:1}
n0_list={0:1, 1:0}
n1_list={0:0, 1:1}

def fibo(num):
	global cache, n0_list, n1_list

	if num==0: 
		return 0
	elif num==1: 
		return 1
	else:
		if not num in cache:
			cache[num]=fibo(num-2)+fibo(num-1) 
			n0_list[num]=n0_list[num-2]+n0_list[num-1]
			n1_list[num]=n1_list[num-2]+n1_list[num-1]
		return cache[num]

num_input=int(input())

for i in range(num_input):
	n=int(input())
	fibo(n)
	print(str(n0_list[n])+" "+str(n1_list[n]))