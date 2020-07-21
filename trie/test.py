expected = {
        "c": {"*": True},
        "b": {"c": {"*": True}, "a": {"b": {"c": {"*": True}}}},
        "a": {"b": {"c": {"*": True}}},
    }
trie = SuffixTrie("babc")
print(trie.root)
print(trie.contains("abc"))
