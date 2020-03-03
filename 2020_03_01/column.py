def solution(n, build_frame):
	answer = []
	#(기둥, 보)
	frame = [[[0,0] for i in range(n+1)] for j in range(n+1)]
		
	for cur in build_frame:
		if cur[3]==1:	#설치
			if cur[2]==0:	#기둥 설치
				if cur[1]==0 or frame[cur[1]-1][cur[0]][0]==1 or (cur[0]!=0 and frame[cur[1]][cur[0]-1][1]==1) or frame[cur[1]][cur[0]][1]==1:
					frame[cur[1]][cur[0]][cur[2]]=1
			else:			#보 설치
				if frame[cur[1]-1][cur[0]][0]==1 or frame[cur[1]-1][cur[0]+1][0]==1 or ((cur[0]!=0 and frame[cur[1]][cur[0]-1][1]==1) and frame[cur[1]][cur[0]+1][1]==1):
					frame[cur[1]][cur[0]][cur[2]]=1
		else:			#삭제
			if cur[2]==0:	#기둥 삭제
				if frame[cur[1]+1][cur[0]][0]==1 and (cur[0]==0 or frame[cur[1]+1][cur[0]-1][1]==0) and frame[cur[1]+1][cur[0]][1]==0 :
					continue
				elif cur[0]!=0 and frame[cur[1]+1][cur[0]-1][1]==1:
					if frame[cur[1]][cur[0]-1][0]==0 and ((cur[0]-1==0 or frame[cur[1]+1][cur[0]-2][1]==0) or frame[cur[1]+1][cur[0]][1]==0):
						continue
				elif cur[0]!=n and frame[cur[1]+1][cur[0]][1]==1:
					if frame[cur[1]][cur[0]+1][0]==0 and ((cur[0]==0 or frame[cur[1]+1][cur[0]-1][1]==0) or frame[cur[1]+1][cur[0]+1][1]==0):
						continue
				frame[cur[1]][cur[0]][0]=0
			else:			#보 삭제
				if cur[0]!=0 and frame[cur[1]][cur[0]-1][1]==1 and frame[cur[1]-1][cur[0]-1][0]==0 and frame[cur[1]-1][cur[0]][0]==0:
					continue
				elif frame[cur[1]][cur[0]][0]==1 and frame[cur[1]-1][cur[0]][0]==0 and (cur[0]==0 or frame[cur[1]][cur[0]-1][1]==0):
					continue
				elif frame[cur[1]][cur[0]+1][0]==1 and frame[cur[1]-1][cur[0]+1][0]==0 and frame[cur[1]][cur[0]+1][1]==0:
					continue
				elif cur[0]!=n-1 and frame[cur[1]][cur[0]+1][1]==1 and frame[cur[1]-1][cur[0]+1][0]==0 and frame[cur[1]-1][cur[0]+2][0]==0:
					continue
				frame[cur[1]][cur[0]][1]=0
	
	for j in range(n+1):
		for i in range(n+1):
			if frame[i][j][0]==1: answer.append([j,i,0])
			if frame[i][j][1]==1: answer.append([j,i,1])
	
	return answer

#x 좌표, y 좌표, (기둥 0, 보 1), (삭제 0, 설치 1)
if __name__ == "__main__":
	build = [[0,0,0,1],[0,1,1,1],[3,0,0,1],[2,1,1,1],[1,1,1,1],[0,1,1,0]]
	print(solution(5,build))