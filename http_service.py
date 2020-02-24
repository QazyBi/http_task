from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib.parse import parse_qs
import string

PORT_NUMBER = 8080

# Server Class
class myHandler(BaseHTTPRequestHandler):
	# List to store user's dictionary
	words_list = []

	# Set headers of the HTTP response
	def _set_headers(self):
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()

	# Handler of GET method
	def do_GET(self):
		global words_list

		# Set Headers of the HTTP reponse
		self._set_headers()

		# In a query keyword starts from 5th character(e.g. /get?word=foobar)
		json_get = parse_qs(self.path[5:])
		
		# Find anagrams of the word
		found_anagrams = anagram_finder(words_list, json_get['word'][0])

		# Send to the client found anagrams
		self.wfile.write(bytes(found_anagrams, 'utf-8'))

	# Handler of the POST method
	def do_POST(self):
		global words_list

		self._set_headers()

		content_length = int(self.headers['Content-Length'])
		# Receive user's dictionary
		post_data = self.rfile.read(content_length)
		
		# Store user's dictionary in class' attribute
		words_list = json.loads(post_data)
	
# Check whether two words have same letters and same amount of them 
def same_letters(word1, word2):
	list1 = [char.lower() for char in word1]
	list2 = [char.lower() for char in word2]

	dict1 = {char : list1.count(char) for char in list1}
	dict2 = {char : list2.count(char) for char in list2}

	for char in dict1.keys():
		if char not in dict2.keys() or dict1[char] != dict2[char]:
			return False

	return True

# Compare each word from the list with target word
def anagram_finder(words_list, trgt_word):
	anagram_list = []

	for word in words_list:
		if same_letters(word, trgt_word.lower()):
			anagram_list.append(word)

	if len(anagram_list) == 0:
		return "null"
	return str(anagram_list).replace('\'', '"').replace(" ", "")


if __name__ == '__main__':
	# Start running the server
	try:
		server = HTTPServer(('', PORT_NUMBER), myHandler)	
		server.serve_forever()
		
	# Stop listening if ^C is pressed
	except KeyboardInterrupt:
		server.socket.close()