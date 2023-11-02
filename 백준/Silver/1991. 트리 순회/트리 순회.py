import sys

class Node:
    def __init__(self,data,left,right):
        self.data = data
        self.left = left
        self.right = right

def preorder(node):
    print(node.data,end="")
    if node.left:
        preorder(tree[node.left])
    if node.right:
        preorder(tree[node.right])
        
def postorder(node):
    if node.left:
        postorder(tree[node.left])
    if node.right:
        postorder(tree[node.right])
    print(node.data,end="")

def inorder(node):
    if node.left:
        inorder(tree[node.left])
    print(node.data,end="")
    if node.right:
        inorder(tree[node.right])
        
tree = {}
n = int(sys.stdin.readline())
for _ in range(n):
    m,l,r = sys.stdin.readline().split()
    if l == '.':
        l = None
    if r == '.':
        r = None
    tree[m] = Node(m,l,r)
    
preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])