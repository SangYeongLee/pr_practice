def solution(left,right):
	answer=0
	cache = [[-1 for i in range(len(left))] for j in range(len(right))]
	return score(0,0,left,right,cache)

def score(l,r,left,right,cache):
	if cache[l][r]!=-1: return cache[l][r]

	if left[l]>right[r]:
		if r+1==len(right):
			cache[l][r]=right[r]
		else:
			cache[l][r]=right[r]+score(l,r+1,left,right,cache)
	else:
		if l+1==len(left):
			cache[l][r]=0
		elif r+1==len(right):
			cache[l][r]=score(l+1,r,left,right,cache)
		else:
			cache[l][r]=max(score(l+1,r,left,right,cache),score(l+1,r+1,left,right,cache))
	
	return cache[l][r]