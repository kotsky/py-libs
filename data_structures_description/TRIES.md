# Trie

Trie is a tree data structure to store characters at each node. Trie has one root node, multiple child nodes and might have end node, which can be presented as some special symbol, like `*`, and can indicate complete words.
![Picture](https://github.com/kotsky/py-libs/blob/master/additional_data/pictures/trie.png)

There are:
	- Prefix Trie (build Trie from the beggining of the string)
	- Suffix Trie (build Trie from the end of the string)
Its implementation is here [Tries](https://github.com/kotsky/py-libs/blob/master/data_structures/tries.py)

## Tries Algorithms / Problems / Usage
Trie is often used to store vocabulary in one place with further easy accessing and searching in linear time.
One classic problem is to find out if the given words are in some text