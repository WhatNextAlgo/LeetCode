ALPHABET_SIZE = 26

class Node:
    def __init__(self,character,value = None):
        self.children = [None for _ in range(ALPHABET_SIZE)]
        self.character = character
        self.leaf = False
        self.value = value # for associative arrays


class Trie:
    def __init__(self):
        self.root = Node("*")
    
    def insert(self,word,value):
        current = self.root
        for char in word:
            ascii_index = ord(char) - ord('a')
            if not current.children[ascii_index]:
                current.children[ascii_index]= Node(char)
            current = current.children[ascii_index]
        current.leaf = True
        current.value = value


    def find(self,word):
        if not self.root.children:
            return None
        current = self.root
        for char in word:
            ascii_index = ord(char) - ord('a')
            if current.children[ascii_index]:
                current = current.children[ascii_index]
            else:
                return None
        if current.leaf:
            return current.value
        return None

    
    def sort(self):
        return self.get_words_prefix("")

    
    def collect(self,node,prefix,words):
        if node is None:
            return None

        if node.leaf:
            words.append(prefix)
        
        for child in node.children:
            if child:
                child_character = child.character
                self.collect(child,prefix + child_character,words)

        return words

    def get_words_prefix(self,prefix):
        current = self.root
        words = []

        for char in prefix:
            ascii_index = ord(char) - ord('a')
            if current.children[ascii_index]:
                current = current.children[ascii_index]
            else:
                return None
        
        return self.collect(current,prefix,words)


if __name__ == "__main__":
    trie = Trie()
    trie.insert("sea",10)
    trie.insert("seashore",12)
    trie.insert("seashell",14)
    trie.insert("bee",16)
    trie.insert("car",18)
    trie.insert("computer",20)

    print(trie.find("sea"))
    print(trie.get_words_prefix("sea"))
    print(trie.sort())