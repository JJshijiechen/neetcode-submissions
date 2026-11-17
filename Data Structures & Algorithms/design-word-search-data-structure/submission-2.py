class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True
        

    def search(self, word: str) -> bool:
        def dfs(node: TrieNode, index: int) -> bool:
            if index == len(word):
                return node.is_word
            
            char = word[index]
            if char == ".":
                return any(
                    dfs(child, index + 1)
                    for child in node.children.values()
                )
            child = node.children.get(char)
            return child is not None and dfs(child, index + 1)

        return dfs(self.root, 0)
