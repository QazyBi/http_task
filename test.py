from http_service import anagram_finder
import unittest

class TestSum(unittest.TestCase):
	def test_word_in_list(self):
		self.assertEqual(anagram_finder(["foobar", "aabb", "baba", "boofar", "test"], "foobar"), "[\"foobar\",\"boofar\"]")

	def test_word_not_in_list(self): 
		self.assertEqual(anagram_finder(["foobar", "aabb", "baba", "boofar", "test"], "raboof"), "[\"foobar\",\"boofar\"]")
		self.assertEqual(anagram_finder(["foobar", "aabb", "baba", "boofar", "test"], "abba"), "[\"aabb\",\"baba\"]")

	def test_one_occurence_in_list(self):
		self.assertEqual(anagram_finder(["foobar", "aabb", "baba", "boofar", "test"], "test"), "[\"test\"]")

	def test_no_anagram_in_list(self):
		self.assertEqual(anagram_finder(["foobar", "aabb", "baba", "boofar", "test"], "qwerty"), "null")


if __name__ == '__main__':
	unittest.main()

