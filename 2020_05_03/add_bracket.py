def operation(n1,n2,op):
	if op=="+":
		return n1+n2
	elif op=="-":
		return n1-n2
	else:
		return n1*n2

def selec(n):
	if n==1:
		return [[0],[1]]
	elif n==2:
		return [[0,0],[0,1],[1,0]]

	ret = []
	#첫 op에 괄호없는 경우
	for s in selec(n-1):
		ret.append([0]+s)

	#첫 op에 괄호있는 경우
	for s in selec(n-2):
		ret.append([1,0]+s)

	return ret

n = int(input())
num = []
op = []

temp = input()
for i in range(len(temp)):
	if i%2==0:
		num.append(int(temp[i]))
	else:
		op.append(temp[i])

if len(op)==0:
	print(num[0])
	exit()

max_val = -(2**31)
for calc in selec(len(op)):
	temp_num = []
	temp_op = []
	op_idx = 0
	num_idx = 0
	while True:
		if calc[op_idx]==0:
			temp_op.append(op[op_idx])
			temp_num.append(num[num_idx])
			op_idx+=1
			num_idx+=1
			if num_idx==len(num)-1: 
				temp_num.append(num[num_idx])
				break
		else:
			temp_num.append(operation(num[num_idx],num[num_idx+1],op[op_idx]))
			if op_idx==len(calc)-1:
				break
			elif op_idx==len(calc)-2:
				temp_op.append(op[op_idx+1])
				temp_num.append(num[-1])
				break
			else:
				temp_op.append(op[op_idx+1])
				num_idx+=2
				op_idx+=2
	
	ans = temp_num[0]
	for i in range(1,len(temp_num)):
		ans = operation(ans,temp_num[i],temp_op[i-1])
	if ans>max_val:
		max_val=ans
print(max_val)