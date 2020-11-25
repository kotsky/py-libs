"""PrefixTrie and SuffixTrie

PrefixTrie Class helps to build vocabulary from the given list, which
contains words as ["this", "yo", "is", "a", "bigger", "string", "kappa"].
Take a note, that in the end of each word after last letter you have 
{'*': int(word_idx)} like for 'foo' -> {'f': {'o': {'o': {'*': 0}}}}
Args:
	list of strings
Returns:
	trie of words/strings
Methods:
	- trie = PrefixTrie(['foo', 'baz']) - by using insert_word method
	add strings to the trie
	- insert_word(string) - insert string to the trie
	- contains(string) - check if the trie has that string -> return bool


SuffixTrie Class creates a trie structure of a string suffixes with 
an end symbol per their index in the initial string.
Args:
	string
Returns:
	trie of suffixes
Methods:
	- trie = SuffixTrie('baz') - by using populate_suffix_trie_from method
	add suffixes of string to the trie
	- populate_suffix_trie_from(string) - insert suffixes of string
	- contains(suffix) - check if the trie has that suffix -> return bool
	
	
Example:
	words = ['foo', 'baz']
	t = PrefixTrie(words)
	s = SuffixTrie(words[0])
	print(s.contains('oo'))
"""

# O(S * N) Time and Space, 
# where S - len of the longest word, 
# and N - len of the word's list

class PrefixTrie:
    def __init__(self, words):
        self.root = {}
        self.end_symbol = '*'
        for word_idx in range(len(words)):
            word = words[word_idx]
            self.insert_word(word, word_idx)

    def insert_word(self, word, word_idx):
        node = self.root
        for i in range(len(word)):
            letter = word[i]
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        node[self.end_symbol] = word_idx

    def contains(self, string):
        node = self.root
        for i in range(len(string)):
            if string[i] in node:
                node = node[string[i]]
            else:
                return False
        return self.end_symbol in node


# O(S) Time and Space, where
# S - len of the input string

class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.end_symbol = "*"
        self.populate_suffix_trie_from(string)

    def populate_suffix_trie_from(self, string):
        for i in range(len(string)):
            node = self.root
            j = i
            while j <= len(string) - 1:
                if string[j] not in node:
                    node[string[j]] = {}
                node = node[string[j]]
                if j == len(string) - 1:
                    node[self.end_symbol] = i
                j += 1

    def contains(self, string):
        node = self.root
        for i in range(len(string)):
            if string[i] in node:
                node = node[string[i]]
            else:
                return False
        return self.end_symbol in node


