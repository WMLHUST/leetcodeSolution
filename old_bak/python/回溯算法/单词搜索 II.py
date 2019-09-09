# coding: utf-8

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

class Solution:
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """

        def findNext(node_stack, ch_stack, board, i, j, markboard, res):
            if markboard[i][j] == 1:
                return

            cur_node = node_stack[-1]
            if board[i][j] not in cur_node.childs:
                return

            # (i,j)在树里
            cur_node = cur_node.childs[board[i][j]]
            ch_stack.append(board[i][j])
            markboard[i][j] = 1
            if cur_node.count>0:
                res.append("".join(ch_stack))

            node_stack.append(cur_node)

            #继续找
            #上
            if i-1>=0 and markboard[i-1][j]==0:
                findNext(node_stack, ch_stack, board, i-1, j, markboard, res)

            # 下
            if i+1<len(board) and markboard[i+1][j]==0:
                findNext(node_stack, ch_stack, board, i+1, j, markboard, res)

            # 左
            if j-1>=0 and markboard[i][j-1]==0:
                findNext(node_stack, ch_stack, board, i, j-1, markboard, res)

            if j+1<len(board[0]) and markboard[i][j+1] == 0:
                findNext(node_stack, ch_stack, board, i, j+1, markboard, res)

            ch_stack.pop()
            node_stack.pop()
            markboard[i][j] = 0


        if len(board)==0 or len(words)==0:
            return []
        row_cnt = len(board)
        col_cnt = len(board[0])

        trie_tree = Trie()
        for item in words:
            trie_tree.insert(item)


        node_stack = [trie_tree.root]
        ch_stack = []
        markboard = [[0] * col_cnt for _ in range(row_cnt)]
        res = []
        for i in range(row_cnt):
            for j in range(col_cnt):
                findNext(node_stack, ch_stack, board, i, j, markboard, res)
        return list(set(res))

board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]

words = ["oath","pea","eat","rain"]

print(Solution().findWords(board, words))









