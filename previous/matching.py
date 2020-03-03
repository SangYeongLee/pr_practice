#a tag안에 url 파싱해서 list return
def parsingLink(text):
	ret = []
	temp = text.split("</a>")
	for i in temp:
		idx = i.find("<a href=\"https://")
		if idx!=-1:
			ret.append(i.split("<a href=\"https://")[1].split("\">")[0])
	return ret

#body안에 tag 제외한 text 단어 단위로 파싱해서 list return
def parsingWord(text):
	ret = []
	temp = text.split("</a>")
	for string in temp:
		idx = string.find("<a href=\"https://")
		i=0
		prev=0
		
		if idx!=-1:
			while i<=idx:
				if not string[i].isalpha():
					if i!=prev:
						ret.append(string[prev:i])
					prev=i+1
				i+=1

			while string[i]!='>': 
				i+=1
			prev=i
			while i<len(string):
				if i==len(string)-1 and i!=prev: ret.append(string[prev:i+1])
				elif not string[i].isalpha():
					if i!=prev:
						ret.append(string[prev:i])
					prev=i+1
				i+=1

		else:
			for i in range(len(string)):
				if i==len(string)-1 and i!=prev: ret.append(string[prev:i+1])
				elif not string[i].isalpha():
					if i!=prev:
						ret.append(string[prev:i])
					prev=i+1
				i+=1
	return ret

def solution(word, pages):
    answer = 0
    word = word.lower()
    url = []
    basic = []	
    score = {}
    link_state = []
    for curr in pages:
    	#html 전체 소문자로
    	curr = curr.lower()

    	#body tag안의 text만 파싱
    	body = curr.split("<body>")[1].split("</body>")[0]
    	#링크 상태 파싱
    	link_state.append(parsingLink(body))
    	
    	#기본점수 채점
    	cnt=0
    	for i in parsingWord(body):
    		if i==word: cnt+=1
    	basic.append(cnt)

    	#head안에 meta tag의 url 파싱해서 딕셔너리에 {url:기본점수} 쌍으로 추가
    	head = curr.split("<head>")[1].split("</head>")[0]
    	url.append(head.split("<meta property=\"og:url\" content=\"https://")[1].split("\"/>")[0])
    	score[url[-1]]=cnt

    #링크 점수 더하기
    for i in range(len(link_state)):
    	for j in link_state[i]:
    		if j in score.keys():
    			score[j]+=(basic[i]/len(link_state[i]))
    
    #최대 인덱스 찾기
    max_score=score[url[0]]
    for i in range(1,len(url)):
    	if max_score<score[url[i]]: 
    		max_score = score[url[i]]
    		answer=i
    
    return answer

word = "muzi"
pages=["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]

print(solution(word,pages))