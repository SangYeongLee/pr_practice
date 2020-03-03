import requests as rq
import json
from bs4 import BeautifulSoup
import queue

# start에 url 넣어주고 해당 url에서 찾을 수 있는 a tag의 href 속성 다 queue에 넣기
class Parse:
	#def __init__(self,start):

	def bfs(self,start):
		search_q = queue.Queue()
		visited = []
		search_q.put(start)

		while not search_q.empty():
			n = search_q.get()	#n <- url
			print("==="+n)
			visited.append(n)
			res = rq.get(n)
			tag = BeautifulSoup(res.text, 'html.parser')
			for url in tag.select('a'):
				print(url.get_text()+"\n"+url.get('href')+"\n")
				search_q.put("https:/"+url.get('href'))

main_parser = Parse()
main_parser.bfs("https://beomi.github.io/beomi.github.io_old/")

#f = open("crawl.txt", 'w')
#req = rq.get("https://beomi.github.io/beomi.github.io_old/")

#f.close()