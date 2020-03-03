cache={1:1,2:2}

n=int(input())

for i in range(3,n+1):
	cache[i]=(cache[i-2]+cache[i-1])%15746

print(cache[n])