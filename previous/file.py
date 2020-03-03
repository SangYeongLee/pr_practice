import re

def solution(files):
	answer = []
	#head - number - tail로 나누는 re
	p = re.compile("([a-z\-\s]+)([0-9]+)(.*)")
	s_list = []

	#head, number, 원본으로 저장
	for temp in files:
		g = p.search(temp.lower())
		head = g.group(1)
		num = int(g.group(2))
		
		s_list.append((head,num,temp))

	#정렬한 후 list 출력
	s_list = sorted(s_list, key=lambda x:(x[0],x[1]))
	for i in s_list:
		answer.append(i[2])

	return answer

def others(files):
	return sorted(files, key = lambda x:(re.compile("([a-z\-\s]+)([0-9]+)(.*)").search(x.lower()).group(1),int(re.compile("([a-z\-\s]+)([0-9]+)(.*)").search(x.lower()).group(2))))

test = ["iamg12", "img10.png", "img02dd33.png", "img1.png", "IMG01.GIF", "img2.JPG"]

print(others(test))
print(solution(test))