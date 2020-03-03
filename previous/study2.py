import math
def powerset(numbers):
	ret=[]
	for i in range(1,2**len(numbers)):
		k=(bin(i)+"")[2:]
		temp=[]
		for j in range(len(k)):
			if k[len(k)-j-1]=="1":
				temp.append(str(numbers[j]))
		if temp not in ret:
			ret.append(temp)

	return ret

def perm(a): 
	length=len(a) 
	if length==1: 
		return [a] 
	else: 
		result=[] 
		for i in a: 
			b=a.copy() 
			b.remove(i) 
			b.sort() 
			for j in perm(b): 
				j.insert(0, i)
				if j not in result: 
					result.append(j)
	return(result)

def checkPrime(num):
	if num==1 or num==0: return False
	for i in range(2,int(math.sqrt(num))+1):
		if num%i==0: return False
	return True

def solution(numbers):
	element = []
	for i in numbers: 
		element.append(i)

	ret=set()
	for j in powerset(element):
		for i in perm(j):
			val = ""
			for j in range(len(i)):
				val+=i[j]
			val = int(val)
			if checkPrime(val):
				ret.add(val)

	return len(ret)

n1="011"
print(solution(n1))