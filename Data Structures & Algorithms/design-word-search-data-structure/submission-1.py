class TrieNode:
    def __init__(self):
        self.children = {}
        self.endsWith = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def getRootNode(self):
        return self.root
    
    def addWord(self, word: str) -> None:
        curr = self.getRootNode()
        for w in word:
            if w not in curr.children:
                node = TrieNode()
                curr.children[w] = node
            curr = curr.children[w]
        curr.endsWith = True
       
    def search(self, word: str) -> bool:
        curr = self.getRootNode()
       
        def checkString(i,curr):
            for w in range(i,len(word)):
                c = word[w]
                if c == '.':
                    for child in curr.children.values():
                        if checkString(w+1,child): return True
                    return False
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
            return curr.endsWith
         
        return checkString(0, curr)
                 
                     


        
