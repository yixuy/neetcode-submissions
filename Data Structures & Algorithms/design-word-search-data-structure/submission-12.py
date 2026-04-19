
class Node:
    def __init__(self, c):
        self.child = defaultdict(Node)
        self.word = ""
        self.char = c

class Trie:
    def __init__(self):
        self.root = Node("")
    def add(self, word):
        curr = self.root

        for c in word:
            if c not in curr.child:
                curr.child[c] = Node(c)
            curr = curr.child[c]

        curr.word = word
    def search(self, word):
        def dfs(root, index):
            curr = root
        
            for i in range(index, len(word)):
                c = word[i]
                if c == ".":
                    for child in curr.child.values():
                        if dfs(child, i + 1):
                            return True
                    return False 
                if c not in curr.child:
                    return False
                curr = curr.child[c]
            return curr.word != ""
        
        return dfs(self.root, 0)

class WordDictionary:

    def __init__(self):
        self.tr = Trie()
        
    def addWord(self, word: str) -> None:
        self.tr.add(word)

    def search(self, word: str) -> bool:
        return self.tr.search(word)
