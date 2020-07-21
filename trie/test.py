def test_case_1(self):
    trie = SuffixTrie("babc")
    expected = {
        "c": {"*": True},
        "b": {"c": {"*": True}, "a": {"b": {"c": {"*": True}}}},
        "a": {"b": {"c": {"*": True}}},
    }
print(trie.root)
print(trie.contains("abc"))
