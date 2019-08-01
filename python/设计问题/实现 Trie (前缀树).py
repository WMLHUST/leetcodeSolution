class Trie:
    class TrieNode():
        def __init__(self,  count=0):
            self.childs = {}
            self.count = count

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = self.TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        cur = self.root
        for i in range(len(word)):
            if word[i] not in cur.childs:
                cur.childs[word[i]] = self.TrieNode()
            cur = cur.childs[word[i]]

        cur.count = 1

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cur = self.root
        for i in range(len(word)):
            if word[i] not in cur.childs:
                return False
            cur = cur.childs[word[i]]

        if cur.count>0:
            return True
        else:
            return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur = self.root
        for i in range(len(prefix)):
            if prefix[i] not in cur.childs:
                return False
            cur = cur.childs[prefix[i]]
        return True

word = 'apple'
obj = Trie()
obj.insert(word)

param_2 = obj.search(word)
print(param_2)

prefix = 'apq'
param_3 = obj.startsWith(prefix)
print(param_3)

