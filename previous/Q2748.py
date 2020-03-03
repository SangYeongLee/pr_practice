cache={1:0, 2:1}

def fibo(num):
	global cache

	if num==0: return 0
	elif num==1: return 1
	else:
		if not num in cache: cache[num]=fibo(num-2)+fibo(num-1)
		return cache[num]

print(2 in cache)
num=int(input())

print(fibo(num))