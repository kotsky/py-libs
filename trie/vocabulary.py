'''
Class below help to build vocabulary from the given list, which
contains words as ["this", "yo", "is", "a", "bigger", "string", "kappa"].
Take a note, that in the end of each word you have {'*': 'wordIdx'}
'''

# O(s * n) TS, where s - len of the longest word, 
# and n - len of the word's list


class Trie:
	def __init__(self, words):
		self.root = {}
		for wordIdx in range(len(words)):
			word = words[wordIdx]
			self.insertWord(word, wordIdx)
	
	def insertWord(self, word, wordIdx):
		node = self.root
		for i in range(len(word)):
			letter = word[i]
			if letter not in node:
				node[letter] = {}
			
			if i == len(word)-1:
				node['*'] = wordIdx
			node = node[letter]
