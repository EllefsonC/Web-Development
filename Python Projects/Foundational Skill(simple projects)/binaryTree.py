# Binary Tree is a non-linear and hierarchical data structure where each node has at most two children referred to as the left child and the right child.  The topmost node in a binary tree is called the root, and the bottom-most nodes are called leaves.

#This script follows the geeksforgeeks tutorial on binary tree and traversal algorithms

#This is the starting code to declare a node of a binary tree
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        
        
firstNode = Node(2)
secondNode = Node(3)
thirdNode = Node(4)
fourthNode = Node(5)

#this creates the tree, with 2 being the root, 3 branching left and 4 branching right, and 5 branching off of value 3 to the left.
firstNode.left = secondNode
firstNode.right = thirdNode
secondNode.left = fourthNode
'''
    2
   / \
  3   4
 /
5
'''
#Searching for values or data in a tree usually falls under 2 traversals, DFS or BFS. BFS is Breadth-First Search which explores all nodes at the current depth before moving on to the next step. ex.  2 then 3,4 then 5. BFS is also referred to as Level Order Traversal. 
#DFS is Depth-First Search explores as far down a branch as possible before checking other branches. This can happen in 3 typical ways, Preorder Traversal: current node, left subtree, then right subtree, In-order Traversal: left subtree, then current node, then right subtree, and Postorder Traversal: left subtree, right subtree, then current node

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

#DFS
#Preorder Traversal: current node, left subtree, then right subtree
def pre_order_dfs(node):
    if node is None:
        return
    print(node.key, end=' ')
    pre_order_dfs(node.left)
    pre_order_dfs(node.right)
 
#In-order Traversal: left subtree, then current node, then right subtree   
def in_order_dfs(node):
    if node is None:
        return
    in_order_dfs(node.left)
    print(node.key, end=' ')
    in_order_dfs(node.right)
    
#Postorder Traversal: left subtree, right subtree, then current node
def post_order_dfs(node):
    if node is None:
        return
    post_order_dfs(node.left)
    post_order_dfs(node.right)
    print(node.key, end=' ')
    
#BFS Breadth-First Search or Level Order Traversal
def bfs(root):
    if root is None:
        return
    queue = [root]
    while queue:
        node = queue.pop(0)
        print(node.key, end=' ')
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
            
#Tangent: if __name__ == "__main__": is used to make code only execute when called upon, this is important if this was a separate file that is called into main.py for a more complex program. If not added the entire code of imported file will be ran even if that is not the intended design.
if __name__ == "__main__":
    root = Node(2)
    root.left = Node(3)
    root.right = Node(4)
    root.left.left = Node(5)

#Root, Left, Right   
print('Pre-Order DFS: ', end=' ')
pre_order_dfs(root)

#Left, Root, Right
print('\nIn-Order DFS: ', end=' ')
in_order_dfs(root)

#Left, Right, Root
print('\nPost-Order DFS: ', end=' ')
post_order_dfs(root)

#Breadth-First Search, searches each level left to right before next level
print('\nBFS is: ', end=' ')
bfs(root)
