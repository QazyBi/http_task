from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib.parse import parse_qs


PORT_NUMBER = 8080

class myHandler(BaseHTTPRequestHandler):
	words_list = []

	def _set_headers(self):
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()

	def do_GET(self):
		global words_list

		json_get = parse_qs(self.path[5:])
		
		found_anagrams = anagram_finder(words_list, json_get['word'][0])

		self._set_headers()
		self.wfile.write(bytes(found_anagrams, 'utf-8'))

	def do_POST(self):
		global words_list

		content_length = int(self.headers['Content-Length'])
		post_data = self.rfile.read(content_length)
		
		words_list = json.loads(post_data)
		self._set_headers()
	

def same_letters(word1, word2):
	list1 = [char for char in word1]
	list2 = [char for char in word2]

	dict1 = {char : list1.count(char) for char in list1}
	dict2 = {char : list2.count(char) for char in list2}

	for char in dict1.keys():
		if char not in dict2.keys() or dict1[char] != dict2[char]:
			return False

	return True

def anagram_finder(words_list, trgt_word):
	anagram_list = []

	for word in words_list:
		if same_letters(word, trgt_word):
			anagram_list.append(word)

	if len(anagram_list) == 0:
		return "null"
	return str(anagram_list).replace('\'', '"').replace(" ", "")


if __name__ == '__main__':
	try:
		server = HTTPServer(('', PORT_NUMBER), myHandler)	
		server.serve_forever()

	except KeyboardInterrupt:
		server.socket.close()