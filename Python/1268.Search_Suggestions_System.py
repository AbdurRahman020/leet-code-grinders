from typing import List
from collections import defaultdict

class TrieNode1:
    def __init__(self):
        self.child_nodes = [None]*26
        self.suggestions = []

class Trie:
    def __init__(self):
        self.root = TrieNode1()

    def insert(self, word):
        current_node = self.root
        
        for char in word:
            index = ord(char) - ord('a')
            
            if current_node.child_nodes[index] is None:
                current_node.child_nodes[index] = TrieNode1()
            
            current_node = current_node.child_nodes[index]
            current_node.suggestions.append(word)
        
        return
    
    def search(self, word):
        current_node = self.root
        
        for char in word:
            index = ord(char) - ord('a')
            if current_node.child_nodes[index] is None:
                return False
            
            current_node = current_node.child_nodes[index]
        
        return current_node.suggestions

class TrieNode2:
    def __init__(self):
        self.child_nodes = defaultdict(TrieNode2)
        self.suggestion = []
    
    def add_suggestion(self, product):
        if len(self.suggestion) < 3:
            self.suggestion.append(product)

class Solution:
    def suggestedProducts1(self, products: List[str], searchWord: str) -> List[List[str]]:
        root = Trie()
        
        for word in products:
            root.insert(word)
        
        suggestions = []
        for i in range(len(searchWord)):
            matching_words = root.search(searchWord[:i+1])
            
            if matching_words:
                suggestions.append(sorted(matching_words)[:3])
            else:
                suggestions.append([])
        
        return suggestions
    
    def suggestedProducts2(self, products: List[str], searchWord: str) -> List[List[str]]:
        product_list = sorted(products)
        root_node = TrieNode2()
        
        for product in product_list:
            curr_node = root_node
            for char in product:
                node = curr_node.child_nodes[char]
                node.add_suggestion(product)
        
        suggestions, node = [], root_node
        
        for char in searchWord:
            node = curr_node.child_nodes[char]
            suggestions.append(node.suggestion)
        
        return suggestions

if __name__ == '__main__':
    s = Solution()
    
    print(s.suggestedProducts1(["mobile","mouse","moneypot","monitor","mousepad"], "mouse"))
    print(s.suggestedProducts1(["havana"], "havana")) 
    
    print(s.suggestedProducts2(["mobile","mouse","moneypot","monitor","mousepad"], "mouse"))
    print(s.suggestedProducts2(["havana"], "havana"))
