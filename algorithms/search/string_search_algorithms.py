"""	String search

- multi_string_search('text', ['str1', 'str2'])
- multi_string_search_v2('text', ['str1', 'str2'])
Example:
	print(multi_string_search("this is a big string",
							["this", "yo", "is", "a", 
							"bigger", "string", "ing"]))
	# [True, False, True, True, False, True, True]

"""

import Tries from py-libs/data_structures


# O(NS + BS) T / O(NS) S
# where N - number of substrings in small_strings
# S - largest len element in small_strings
# B - len of big_string

def multi_string_search(big_string, small_strings):

    def _search_helper(string, tier, idx, is_contained):
        node = tier.root
        while idx < len(string):
            if string[idx] not in node:
                break
            else:
                node = node[string[idx]]
                idx += 1
            if '*' in node:
                is_contained[node['*']] = True
                if len(node) == 1:
                    break

    is_in_string = [False] * len(small_strings)
    tiers = PrefixTrie(small_strings)

    for i in range(len(big_string)):
        _search_helper(big_string, tiers, i, is_in_string)
    return is_in_string
	
	
# O(BN+SN) T average and O(BNS) T worst / O(N) S

def multi_string_search_v2(big_string, small_strings):
    isInString = []
	for word in small_strings:	
		#isInString.append(word in big_string)
		isInString.append(big_string.find(word) >= 0)	
		
	return isInString
