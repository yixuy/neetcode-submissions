class Node:
    def __init__(self, c):

        self.child = defaultdict(Node)
        self.char = c
        self.word = ""
        # {"A": Node(A)}
class PrefixTree:

    def __init__(self):
        self.root = Node('')

    def insert(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.child:
                curr.child[c] = Node(c)
            curr = curr.child[c]

        curr.word = word

    def search(self, word: str) -> bool:
        curr = self.root
        child = curr.child 
        
        for c in word:
            if c not in child:
                return False 
            else:
                curr =  child[c]
                child = curr.child 

        return curr.word == word 
    

    def startsWith(self, prefix: str) -> bool:

        curr = self.root
        child = curr.child 
        res = True 
        
        for c in prefix:
            if c not in child:
                return False 
            else:
                curr =  child[c]
                child = curr.child 

        return True
        
        