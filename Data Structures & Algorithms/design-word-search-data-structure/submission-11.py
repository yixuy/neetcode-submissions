class WordDictionary:

    def __init__(self):
        self.words = []

    def addWord(self, word: str) -> None:
        self.words.append(word)        

    def search(self, word: str) -> bool:
        for w in self.words:
            if len(w) != len(word):
                continue
            count = 0
            for i in range(len(w)):
                if w[i] == word[i] or word[i] == '.':
                    count += 1

            if len(w) == count :
                return True
        return False
        
