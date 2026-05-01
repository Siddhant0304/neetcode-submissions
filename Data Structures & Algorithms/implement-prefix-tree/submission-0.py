class TrieNode:
    def __init__(self):
        self.children = {}
        self.endsWith = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        
        curr = self.root
        for w in word:
            if w not in curr.children:
                node = TrieNode()
                curr.children[w] = node    
            curr = curr.children[w]
        curr.endsWith = True

    def search(self, word: str) -> bool:
        curr = self.root
        for w in word:
            if w not in curr.children:
                return False
            curr = curr.children[w]
        if curr.endsWith:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for w in prefix:
            if w not in curr.children:
                return False
            curr = curr.children[w]
        
        return True
        
        