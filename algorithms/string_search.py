"""	String search

print(multi_string_search("this is a big string",
                        ["this", "yo", "is", "a", 
						"bigger", "string", "ing"]))
# [True, False, True, True, False, True, True]

"""

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