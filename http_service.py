# assert anagram_finder(["foobar", "aabb", "baba", "boofar", "test"], "foobar"), ["barfoo"]
# curl 'localhost:8080/get?word=foobar' => ["foobar","boofar"]
# curl 'localhost:8080/get?word=raboof' => ["foobar","boofar"]
# curl 'localhost:8080/get?word=abba' => ["aabb","baba"]
# curl 'localhost:8080/get?word=test' => ["test"]
# curl 'localhost:8080/get?word=qwerty' => null

# print(anagram_finder(words, target))	
# * написать юнит-тесты
# ** сделать возможность поднять проект с помощью docker-compose up



from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import cgi
from urllib.parse import parse_qs
import logging


PORT_NUMBER = 8080

class myHandler(BaseHTTPRequestHandler):
	word_list = []

	# def __init__(self, request, client_address, server):
	# 	BaseHTTPRequestHandler.__init__(self, request, client_address, server)

	def _set_headers(self):
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()

	# def _set_word_list(self, value):
	# 	self.word_list = value

	def do_GET(self):
		global word_list

		print(word_list)
		json_get = parse_qs(self.path[5:])
		
		val = self.anagram_finder(word_list, json_get['word'][0])

		self._set_headers()
		self.wfile.write(bytes(val, 'utf-8'))

	def do_POST(self):
		global word_list

		content_length = int(self.headers['Content-Length'])
		post_data = self.rfile.read(content_length)
		
		word_list = json.loads(post_data)

		print(word_list)
		self._set_headers()
		
	def same_letters(self, word1, word2):
		list1 = [char for char in word1]
		list2 = [char for char in word2]

		dict1 = {char : list1.count(char) for char in list1}
		dict2 = {char : list2.count(char) for char in list2}

		for char in dict1.keys():
			if char not in dict2.keys() or dict1[char] != dict2[char]:
				return False
	
		return True


	# if word in list then include it
	# if word not in the list then not include it

	def anagram_finder(self, words_list, trgt_word):
		anagram_list = []

		for word in words_list:
			if self.same_letters(word, trgt_word):
				anagram_list.append(word)

		if len(anagram_list) == 0:
			return 'null\n'
		return str(anagram_list) + '\n'


try:
	#Create a web server and define the handler to manage the
	#incoming request
	server = HTTPServer(('', PORT_NUMBER), myHandler)
	print('Started httpserver on port ' , PORT_NUMBER)
	
	#Wait forever for incoming htto requests
	server.serve_forever()

except KeyboardInterrupt:
	print('\n^C received, shutting down the web server')
	server.socket.close()