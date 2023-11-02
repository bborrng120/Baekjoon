import sys
sys.setrecursionlimit(100000)

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
class BinaryTree:
    def __init__(self):
        self.root = None
        
    def insert(self,node):
        if not self.root:
            self.root = node
        else:
            current = self.root
            
            while True:
                if current.data > node.data:
                    if not current.left:
                        current.left = node
                        break
                    else:
                        current = current.left
                else:
                    if not current.right:
                        current.right = node
                        break
                    else:
                        current = current.right
                        
    def postorder(self,node):
        if node.left:
            self.postorder(node.left)
        if node.right:
            self.postorder(node.right)
        print(node.data)
                        
tree = BinaryTree()
while True:
    try:
        n = int(sys.stdin.readline())
        node = Node(n)
        tree.insert(node)
    except:
        break

tree.postorder(tree.root)