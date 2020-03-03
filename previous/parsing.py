import requests as rq
import json
from bs4 import BeautifulSoup
import queue

#f = open("crawl.txt", 'w')
req = rq.get("https://beomi.github.io/beomi.github.io_old/")
q = queue.Queue()

# html code, header, http status
html = req.text
header = req.headers
status = req.status_code

#html code를 python 내장 html parser로 parsing
soup = BeautifulSoup(html, 'html.parser')

#a tag의 text들 다 뽑아온거 & url queue에 넣기
for a_tag in soup.select('h3 > a'):
	print(a_tag.get_text()+"\n"+a_tag.get('href')+"\n")
	#f.write(a_tag.get_text()+"\n")
	q.put(a_tag.get('href'))

#for q_element in range(q.qsize()):
#	print(q.get())

test="https://beomi.github.io"+q.get()  #이러니까 되긴함
print(test)
req = rq.get(test)

soup = BeautifulSoup(req.text, 'html.parser')
#print()

#f.close()