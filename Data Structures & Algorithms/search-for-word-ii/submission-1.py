class TrieNode:
    def __init__(self):
        self.word = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        wordTrie = Trie()

        for word in words:
            wordTrie.insert(word)

        res, visit = set(), set()

        def dfs(i, j, cur, word):

            if (i < 0 or i >= len(board) or 
                j < 0 or j >= len(board[0]) or 
                (i, j) in visit or 
                board[i][j] not in cur.children):
                return
            
            c = board[i][j]
            visit.add((i, j))
            word += c
            cur = cur.children[c]

            if cur.word:
                res.add(word)

            dfs(i + 1, j, cur, word)
            dfs(i - 1, j, cur, word)
            dfs(i, j + 1, cur, word)
            dfs(i, j - 1, cur, word)

            visit.remove((i, j))
            word = word[:-1]

        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, wordTrie.root, "")

        return list(res)
