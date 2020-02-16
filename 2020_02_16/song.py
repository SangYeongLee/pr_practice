import re

# #음을 소문자로 변환하는 함수
def trimMelody(song):
	ret=""
	info = re.compile('[A-G]#?').findall(song)
	for i in info:
		if len(i)==2:
			ret+=i[0].lower()
		else:
			ret+=i
	return ret

# hh:mm 형태의 시간을 정수로 변환하는 함수
def ttoi(time):
	ret = int(time[0:2])*60+int(time[3:5])
	return ret

# 재생 시간만큼 멜로디 맞추는 함수
def melody(time,song):
	ret=""
	for i in range(time):
		ret+=song[i%len(song)]
	return ret

def solution(m, musicinfos):
	answer = ""
	maxTime = 0
	m = trimMelody(m)	# 기억하고 있는 멜로디를 정리
	
	for temp in musicinfos:
		music = temp.split(',')
		t = ttoi(music[1])-ttoi(music[0])
		music[3] = trimMelody(music[3])
		info = melody(t,music[3])

		# 곡의 멜로디에 기억하고 있는 멜로디가 있고 재생 시간이 최대일 때
		if info.find(m)!=-1 and maxTime<t:
			maxTime = t
			answer = music[2]

	# 매칭되는게 없으면
	if maxTime==0: return "(None)"

	return answer

test = ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,TEST,ABCD#E", "13:00,13:05,WORLD,ABCDEF"]
a = "as,abc,fga"

#print(melody(13,"A#BFGG#AA"))
print(solution("ABG",test))