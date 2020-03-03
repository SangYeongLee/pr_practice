def divisors(number):
	ret=[]
	i=3
	while i*i <= number:
		if number%i==0:
			ret.append(i)
		i+=1

	return ret

def solution(brown, red):
    answer = []
    numTile = brown+red
    div = divisors(numTile)
    for rows in div:
    	columns=int(numTile/rows)
    	b=2*(rows+columns)-4
    	r=(rows-2)*(columns-2)
    	if b==brown and r==red:
    		answer = [columns,rows]
    		break

    return answer

print(solution(10,2))