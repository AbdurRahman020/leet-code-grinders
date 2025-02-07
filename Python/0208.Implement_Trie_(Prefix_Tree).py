class TrieNode:
    def __init__(self):
        self.child_nodes = [None] * 26
        self.is_complete_word = False

class Trie:
    def __init__(self):
        self.root_node = TrieNode()
    
    def insert(self, word: str) -> None:
        curr_node = self.root_node
        
        for letter in word:
            pos = ord(letter) - ord('a')
            if curr_node.child_nodes[pos] is None:
                curr_node.child_nodes[pos] = TrieNode()
            
            curr_node = curr_node.child_nodes[pos]
        
        curr_node.is_complete_word = True
    
    def search(self, word: str) -> bool:
        curr_node = self.root_node
        
        for letter in word:
            pos = ord(letter) - ord('a')
            if curr_node.child_nodes[pos] is None:
                return False
            
            curr_node = curr_node.child_nodes[pos]
        
        return curr_node.is_complete_word
    
    def startsWith(self, prefix: str) -> bool:
        curr_node = self.root_node
        
        for letter in prefix:
            pos = ord(letter) - ord('a')
            if curr_node.child_nodes[pos] is None:
                return False
            
            curr_node = curr_node.child_nodes[pos]
        
        return True

if __name__ == '__main__':
    trie = Trie()
    
    trie.insert("apple")
    trie.insert("app")
    
    search_results = {
        "apple": trie.search("apple"),
        "app": trie.search("app"),
        "appl": trie.search("appl"),
        "banana": trie.search("banana")
    }
    
    prefix_results = {
        "app": trie.startsWith("app"),
        "ap": trie.startsWith("ap"),
        "banana": trie.startsWith("banana")
    }
    
    print("Search Results:")
    for word, result in search_results.items():
        print(f"{word}: {result}")
        
    print("\nPrefix Results:")
    for prefix, result in prefix_results.items():
        print(f"{prefix}: {result}")