BOARD_SIZE = 3

class BoggleGame:
    def __init__(self,boggle_table):
        self.boggle_table = boggle_table
        self.tree = TernarySearchTree()
        self.visited = [[False for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        
    
    def is_valid(self,r,c):
        if (r < 0 or r >= BOARD_SIZE or c < 0 or c >= BOARD_SIZE or
            self.visited[r][c]):
            return False
        return True

    def search(self, row,col,s):
        if self.tree.find(s):
            print(s)
        
        if self.is_valid(row,col):
            self.visited[row][col] =True

            if self.is_valid(row -1 ,col):
                self.search(row -1,col, s + self.boggle_table[row-1][col])

            if self.is_valid(row + 1 ,col):
                self.search(row + 1,col, s + self.boggle_table[row+1][col])

            if self.is_valid(row,col -1 ):
                self.search(row,col -1 , s + self.boggle_table[row][col -1])

            if self.is_valid(row,col + 1):
                self.search(row,col + 1, s + self.boggle_table[row][col + 1])

            self.visited[row][col] = False



    def find_words(self):
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                self.search(i,j,"" + self.boggle_table[i][j])
        



class Node:
    def __init__(self,character):
        self.character = character
        self.left = None
        self.middle = None
        self.right = None
        self.leaf = False

class TernarySearchTree:
    def __init__(self):
        self.root = None

        self.put('dog')
        self.put('computer')

    def put(self, word):
        self.root = self.insert(self.root,word,0)

    def insert(self,node,word,index):
        c = word[index]
        if not node:
            node = Node(c)

        if c < node.character:
            node.left = self.insert(node.left,word,index)
        elif c > node.character:
            node.right = self.insert(node.right,word,index)
        elif index < len(word) -1:
            node.middle= self.insert(node.middle,word, index + 1)
        else:
            node.leaf = True


        return node

    def find(self,word):
        node = self.retrieve(self.root,word,0)
        if node is None:
            return False
        
        return node.leaf

    
    def retrieve(self,node,word,index):
        if node is None:
            return None

        c = word[index]

        if c < node.character:
            return self.retrieve(node.left,word,index)
        elif c > node.character:
            return self.retrieve(node.right,word,index)
        elif index < len(word) -1:
            return self.retrieve(node.middle,word,index + 1)
        else:
            if not node.leaf:
                return None
            return node

    def traverse_tree(self,node,s):
        if node.value is not None:
            print("{0} - {1}".format(s + node.character,node.value))

        if node.left is not None:
            self.traverse_tree(node.left,s)

        if node.middle is not None:
            self.traverse_tree(node.middle,s + node.character)

        if node.right is not None:
            self.traverse_tree(node.right,s)

    def traverse(self):
        if self.root is not None:
            self.traverse_tree(self.root,'')


if __name__ == "__main__":
    table = [
            ['a','c','r'],
            ['m','o','e'],
            ['p','u','t']]
    game = BoggleGame(table)
    game.find_words()
