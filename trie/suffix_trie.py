class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    def populateSuffixTrieFrom(self, string):
        for i in range(len(string)):
            node = self.root
            j = i
            while j <= len(string) - 1:
                if string[j] not in node:
                    node[string[j]] = {}
                node = node[string[j]]
                if j == len(string) - 1:
                    node[self.endSymbol] = True
                j += 1

    def contains(self, string):
        node = self.root
        for i in range(len(string)):
            if string[i] in node:
                node = node[string[i]]
            else:
                return False
        return self.endSymbol in node

