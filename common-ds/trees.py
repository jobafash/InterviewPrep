# Trees consist of vertices (nodes) and edges that connect them. Unlike the linear data structures that we have studied so far, trees are hierarchical. They are similar to Graphs, except that a cycle cannot exist in a Tree - they are acyclic. In other words, there is always exactly one path between any two nodes.

#     Root Node: A node with no parent nodes. Generally, trees don’t have to have a root. However, rooted trees have one distinguished node and are largely what we will use in this course.
#     Child Node: A Node which is linked to an upper node (Parent Node)
#     Parent Nodes: A Node that has links to one or more Child Nodes
#     Sibling Node: Nodes that share same Parent Node
#     Leaf Node: A node that doesn’t have any Child Node
#     Ancestor Nodes: the nodes on the path from a node d to the root node. Ancestor nodes include node d’s parents, grandparents, and so on



    # Sub-tree: For a particular non-leaf node, a collection of nodes, essentially the tree, starting from its child node. The tree formed by a node and its descendants.

    # Degree of a node: Total number of children of a node

    # Length of a path: The number of edges in a path

    # Depth of a node n: The length of the path from a node n to the root node. The depth of the root node is 0.

    # Level of a node n: (Depth of a Node)+1

    # Height of a node n: The length of the path from n to its deepest descendant. So the height of the tree itself is the height of the root node and the height of leaf nodes is always 0.

    # Height of a Tree: Height of its root node

#Types

    # Binary Trees
    # Binary Search Trees
    # AVL Trees
    # Red-Black Trees
    # 2-3 Trees

#The N-ary Tree 

#In graph theory, an N-ary tree is a rooted tree in which each node has no more than N children. It is also sometimes known as a k-way tree, a k-ary tree, or an M-ary tree. A binary tree is a special case where k=2, so they can have a maximum of 2 child nodes and a minimum of 0 child nodes. Binary trees are used extensively in a plethora of important algorithms!

'''
A binary tree is height-balanced if, for each node in the tree, the difference between the height of the right subtree and the left subtree is at most one.

∣Height(LeftSubTree)−Height(RightSubTree)∣<=1|Height(LeftSubTree) - Height(RightSubTree) |<= 1 ∣Height(LeftSubTree)−Height(RightSubTree)∣<=1

A complete binary tree is a binary tree in which all the levels of the tree are fully filled, except for perhaps the last level which can be filled from left to right.


    In a full or ‘proper’ binary tree, every node has 0 or 2 children. No node can have 1 child.
    The total number of nodes in a full binary tree of height ‘h’ can be expressed as:

2h+1 ≤ total number of nodes ≤ 2^(h+1) − 1

A Binary tree is said to be Perfect if all its internal nodes have two children and all leaves are at the same level. Also note that,

    the total number of nodes in a perfect binary tree of height ‘h’ are given as: 2(h+1)−12^{(h+1)}-12​(h+1)​​−1
    the total number of leaf nodes are given as 2hor(n+1)22^{h} or \frac{(n+1)}{2}2​h​​or​2​​(n+1)​​

Skewed Binary Trees are Binary trees such that all the nodes except one have one and only one child. All of the children nodes are either left or right child nodes so the entire tree is positioned to the left or the right side. This type of Binary Tree structure should be avoided at all costs because the time complexity of most operations will be high


'''


'''
Binary Search Trees (BSTs) are a special kind of binary tree where each node of the tree has key-value pairs. These key-value pairs can be anything, like (username,bank)(username,bank)(username,bank) or (employee,employeeID)(employee, employeeID)(employee,employeeID). For all the nodes in a BST, the values of all the keys in the left sub-tree of the node are less than the value of the nodes themselves. All the keys in the right subtree are greater than the values of the node. This is referred to as the BST rule.

NodeValues(leftsubtree)<=CurrentNodeValue<NodeValues(rightsubtree)NodeValues(left subtree)<=CurrentNodeValue<NodeValues(right subtree)NodeValues(leftsubtree)<=CurrentNodeValue<NodeValues(rightsubtree)

'''
class Node:
    def __init__(self, val):  # Constructor to initialize the value of the node
        self.val = val
        self.leftChild = None  # Sets the left and right children to `None`
        self.rightChild = None
        self.parent = None  # Sets the parent to `None`
    
    def insert(self, val):
        current = self
        parent = None
        while current:
            parent = current
            if val < current.val:
                current = current.leftChild
            else:
                current = current.rightChild

        if(val < parent.val):
            parent.leftChild = Node(val)
        else:
            parent.rightChild = Node(val)
    #Recursive
    def insert(self, val):
        if val < self.val:
            if self.leftChild:
                self.leftChild.insert(val)
            else:
                self.leftChild = Node(val)
                return
        else:
            if self.rightChild:
                self.rightChild.insert(val)
            else:
                self.rightChild = Node(val)
                return
    

class BinarySearchTree:
    def __init__(self, val):  # Initializes a root node
        self.root = Node(val)
    
    def insert(self, val):
        if self.root:
            return self.root.insert(val)
        else:
            self.root = Node(val)
            return True
    #Recursive
    def insert(self, val):
        if self.root:
            return self.root.insert(val)
        else:
            self.root = Node(val)
            return True

BST = BinarySearchTree(6)  # Initializes a BST
print(BST.root.val)

'''
description of the algorithm you’d use to insert a new value into a BST.

    Start from the root node

    Check if the value to be inserted is greater than the root/current node’s value

    If yes, then repeat the steps above for the right subtree, otherwise repeat the steps above for the left sub-tree of the current node.

    Repeat until you find a node that has no right/left child to move onto. Insert the given value there and update the parent node accordingly.
Iterative

The insert(val) function takes an integer value and if the root exists, it calls the Node class’s insert function on it; otherwise, it makes the root the value to be inserted. The Node class’s insert() function takes care of the meat of the algorithm. Now, while you can write an insert function in the BinarySearchTree class itself, it’s better to write it as part of the Node class as it usually makes the code cleaner and easier to maintain.

The insert(val) function starts from the root of the tree and moves on to the left or right sub-tree depending on whether the value to be inserted is less than or greater than or equal to the node. While traversing, it stores the parent node of each current node and when the current node becomes empty or None, it inserts the value there. It does so by making the value to be inserted the current node (which is None)'s parent’s child. In other words, the value is inserted in place of the current node.

Recursive

This implementation starts with the root and calls the insert function on its left child if val is less than the value at the root, and calls it on its right child if val is greater than or equal to the value at the root. This continues until a None node is reached. At that point, a new node is created and returned to the previous leaf node, which is now the parent of the new node that we just created.
'''
import random
def display(node):
    lines, _, _, _ = _display_aux(node)
    for line in lines:
        print(line)


def _display_aux(node):
    """
    Returns list of strings, width, height,
    and horizontal coordinate of the root.
    """
    # No child.
    if node.rightChild is None and node.leftChild is None:
        line = str(node.val)
        width = len(line)
        height = 1
        middle = width // 2
        return [line], width, height, middle

    # Only left child.
    if node.rightChild is None:
        lines, n, p, x = _display_aux(node.leftChild)
        s = str(node.val)
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
        second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
        shifted_lines = [line + u * ' ' for line in lines]
        final_lines = [first_line, second_line] + shifted_lines
        return final_lines, n + u, p + 2, n + u // 2

    # Only right child.
    if node.leftChild is None:
        lines, n, p, x = _display_aux(node.rightChild)
        s = str(node.val)
        u = len(s)
#        first_line = s + x * '_' + (n - x) * ' '
        first_line = s + x * '_' + (n - x) * ' '
        second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
        shifted_lines = [u * ' ' + line for line in lines]
        final_lines = [first_line, second_line] + shifted_lines
        return final_lines, n + u, p + 2, u // 2

    # Two children.
    left, n, p, x = _display_aux(node.leftChild)
    right, m, q, y = _display_aux(node.rightChild)
    s = '%s' % node.val
    u = len(s)
    first_line = (x + 1) * ' ' + (n - x - 1) * \
        '_' + s + y * '_' + (m - y) * ' '
    second_line = x * ' ' + '/' + \
        (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
    if p < q:
        left += [n * ' '] * (q - p)
    elif q < p:
        right += [m * ' '] * (p - q)
    zipped_lines = zip(left, right)
    lines = [first_line, second_line] + \
        [a + u * ' ' + b for a, b in zipped_lines]
    return lines, n + m + u, max(p, q) + 2, n + u // 2

'''
Searching in a Binary Search Tree (Implementation)



    Set the ‘current node’ equal to root.

    If the value is less than the ‘current node’s’ value, then move on to the left-subtree otherwise move on to the right sub-tree

    Repeat until the value at the ‘current node’ is equal to the value searched or it becomes None.

    Return the current node
Explain: In this implementation, the core of the search function is implemented in the Node class. The BinarySearchTree first checks if root is None, if so, it returns False, otherwise, it calls the Node class’s search() function on the root.

The search function sets current to self and goes into a while loop which traverses the tree comparing val to the values of the left and right child nodes. If val is less than the value at the current node, we move on to the left subtree and if it is greater, we move on to the right subtree until we reach a leaf node or the value being searched for.
'''
def display(node):
    lines, _, _, _ = _display_aux(node)
    for line in lines:
        print(line)


def _display_aux(node):
    """
    Returns list of strings, width, height,
    and horizontal coordinate of the root.
    """
    # No child.
    if node.rightChild is None and node.leftChild is None:
        line = str(node.val)
        width = len(line)
        height = 1
        middle = width // 2
        return [line], width, height, middle

    # Only left child.
    if node.rightChild is None:
        lines, n, p, x = _display_aux(node.leftChild)
        s = str(node.val)
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
        second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
        shifted_lines = [line + u * ' ' for line in lines]
        final_lines = [first_line, second_line] + shifted_lines
        return final_lines, n + u, p + 2, n + u // 2

    # Only right child.
    if node.leftChild is None:
        lines, n, p, x = _display_aux(node.rightChild)
        s = str(node.val)
        u = len(s)
#        first_line = s + x * '_' + (n - x) * ' '
        first_line = s + x * '_' + (n - x) * ' '
        second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
        shifted_lines = [u * ' ' + line for line in lines]
        final_lines = [first_line, second_line] + shifted_lines
        return final_lines, n + u, p + 2, u // 2

    # Two children.
    left, n, p, x = _display_aux(node.leftChild)
    right, m, q, y = _display_aux(node.rightChild)
    s = '%s' % node.val
    u = len(s)
    first_line = (x + 1) * ' ' + (n - x - 1) * \
        '_' + s + y * '_' + (m - y) * ' '
    second_line = x * ' ' + '/' + \
        (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
    if p < q:
        left += [n * ' '] * (q - p)
    elif q < p:
        right += [m * ' '] * (p - q)
    zipped_lines = zip(left, right)
    lines = [first_line, second_line] + \
        [a + u * ' ' + b for a, b in zipped_lines]
    return lines, n + m + u, max(p, q) + 2, n + u // 2

class Node:
    def __init__(self, val):
        self.val = val
        self.leftChild = None
        self.rightChild = None

    def insert(self, val):
        if self is None:
            self = Node(val)
            return
        current = self

        while current:
            parent = current
            if val < current.val:
                current = current.leftChild
            else:
                current = current.rightChild

        if(val < parent.val):
            parent.leftChild = Node(val)
        else:
            parent.rightChild = Node(val)

    def search(self, val):
        current = self
        while current is not None:
            if val < current.val:
                current = current.leftChild
            elif val > current.val:
                current = current.rightChild
            else:
                return True
        return False
    def search(self, val):
        if val < self.val:
            if self.leftChild:
                return self.leftChild.search(val)
            else:
                return False
        elif val > self.val:
            if self.rightChild:
                return self.rightChild.search(val)
            else:
                return False
        else:
            return True

class BinarySearchTree:
    def __init__(self, val):
        self.root = Node(val)

    def insert(self, val):
        if self.root:
            return self.root.insert(val)
        else:
            self.root = Node(val)
            return True

    def search(self, val):
        if self.root:
            return self.root.search(val)
        else:
            return False


##Recursive

def display(node):
    lines, _, _, _ = _display_aux(node)
    for line in lines:
        print(line)


def _display_aux(node):
    """
    Returns list of strings, width, height,
    and horizontal coordinate of the root.
    """
    # No child.
    if node.rightChild is None and node.leftChild is None:
        line = str(node.val)
        width = len(line)
        height = 1
        middle = width // 2
        return [line], width, height, middle

    # Only left child.
    if node.rightChild is None:
        lines, n, p, x = _display_aux(node.leftChild)
        s = str(node.val)
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
        second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
        shifted_lines = [line + u * ' ' for line in lines]
        final_lines = [first_line, second_line] + shifted_lines
        return final_lines, n + u, p + 2, n + u // 2

    # Only right child.
    if node.leftChild is None:
        lines, n, p, x = _display_aux(node.rightChild)
        s = str(node.val)
        u = len(s)
#        first_line = s + x * '_' + (n - x) * ' '
        first_line = s + x * '_' + (n - x) * ' '
        second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
        shifted_lines = [u * ' ' + line for line in lines]
        final_lines = [first_line, second_line] + shifted_lines
        return final_lines, n + u, p + 2, u // 2

    # Two children.
    left, n, p, x = _display_aux(node.leftChild)
    right, m, q, y = _display_aux(node.rightChild)
    s = '%s' % node.val
    u = len(s)
    first_line = (x + 1) * ' ' + (n - x - 1) * \
        '_' + s + y * '_' + (m - y) * ' '
    second_line = x * ' ' + '/' + \
        (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
    if p < q:
        left += [n * ' '] * (q - p)
    elif q < p:
        right += [m * ' '] * (p - q)
    zipped_lines = zip(left, right)
    lines = [first_line, second_line] + \
        [a + u * ' ' + b for a, b in zipped_lines]
    return lines, n + m + u, max(p, q) + 2, n + u // 2


BST = BinarySearchTree(50)
for _ in range(15):
    ele = random.randint(0, 100)
    BST.insert(ele)

# We have hidden the code for this function but it is available for use!
display(BST.root)
print('\n')

print(BST.search(15))
print(BST.search(50))


#Deletion in a Binary Search Tree
'''

    Deleting in an empty tree
    Deleting a node with no children, i.e., a leaf node.
    Deleting a node which has one child only
        Deleting a node which has a right child only
        Deleting a node which has a left child only
    Deleting a node with two children


'''
def delete(self, val):
        if self.root is not None:
            self.root = self.root.delete(val)
#1

def display(node):
    lines, _, _, _ = _display_aux(node)
    for line in lines:
        print(line)


def _display_aux(node):
    """
    Returns list of strings, width, height,
    and horizontal coordinate of the root.
    """
    # None.
    if node is None:
        line = 'Empty tree!'
        width = len(line)
        height = 1
        middle = width // 2
        return [line], width, height, middle

    # No child.
    if node.rightChild is None and node.leftChild is None:
        line = str(node.val)
        width = len(line)
        height = 1
        middle = width // 2
        return [line], width, height, middle

    # Only left child.
    if node.rightChild is None:
        lines, n, p, x = _display_aux(node.leftChild)
        s = str(node.val)
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
        second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
        shifted_lines = [line + u * ' ' for line in lines]
        final_lines = [first_line, second_line] + shifted_lines
        return final_lines, n + u, p + 2, n + u // 2

    # Only right child.
    if node.leftChild is None:
        lines, n, p, x = _display_aux(node.rightChild)
        s = str(node.val)
        u = len(s)
#        first_line = s + x * '_' + (n - x) * ' '
        first_line = s + x * '_' + (n - x) * ' '
        second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
        shifted_lines = [u * ' ' + line for line in lines]
        final_lines = [first_line, second_line] + shifted_lines
        return final_lines, n + u, p + 2, u // 2

    # Two children.
    left, n, p, x = _display_aux(node.leftChild)
    right, m, q, y = _display_aux(node.rightChild)
    s = '%s' % node.val
    u = len(s)
    first_line = (x + 1) * ' ' + (n - x - 1) * \
        '_' + s + y * '_' + (m - y) * ' '
    second_line = x * ' ' + '/' + \
        (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
    if p < q:
        left += [n * ' '] * (q - p)
    elif q < p:
        right += [m * ' '] * (p - q)
    zipped_lines = zip(left, right)
    lines = [first_line, second_line] + \
        [a + u * ' ' + b for a, b in zipped_lines]
    return lines, n + m + u, max(p, q) + 2, n + u // 2


BST = BinarySearchTree(50)
print("tree:")
display(BST.root)

BST.delete(50)
BST.delete(50)  # Deleting in an empty tree
display(BST.root)

def display(node):
    lines, _, _, _ = _display_aux(node)
    for line in lines:
        print(line)


def _display_aux(node):
    """
    Returns list of strings, width, height,
    and horizontal coordinate of the root.
    """
    # None.
    if node is None:
        line = 'Empty tree!'
        width = len(line)
        height = 1
        middle = width // 2
        return [line], width, height, middle

    # No child.
    if node.rightChild is None and node.leftChild is None:
        line = str(node.val)
        width = len(line)
        height = 1
        middle = width // 2
        return [line], width, height, middle

    # Only left child.
    if node.rightChild is None:
        lines, n, p, x = _display_aux(node.leftChild)
        s = str(node.val)
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
        second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
        shifted_lines = [line + u * ' ' for line in lines]
        final_lines = [first_line, second_line] + shifted_lines
        return final_lines, n + u, p + 2, n + u // 2

    # Only right child.
    if node.leftChild is None:
        lines, n, p, x = _display_aux(node.rightChild)
        s = str(node.val)
        u = len(s)
#        first_line = s + x * '_' + (n - x) * ' '
        first_line = s + x * '_' + (n - x) * ' '
        second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
        shifted_lines = [u * ' ' + line for line in lines]
        final_lines = [first_line, second_line] + shifted_lines
        return final_lines, n + u, p + 2, u // 2

    # Two children.
    left, n, p, x = _display_aux(node.leftChild)
    right, m, q, y = _display_aux(node.rightChild)
    s = '%s' % node.val
    u = len(s)
    first_line = (x + 1) * ' ' + (n - x - 1) * \
        '_' + s + y * '_' + (m - y) * ' '
    second_line = x * ' ' + '/' + \
        (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
    if p < q:
        left += [n * ' '] * (q - p)
    elif q < p:
        right += [m * ' '] * (p - q)
    zipped_lines = zip(left, right)
    lines = [first_line, second_line] + \
        [a + u * ' ' + b for a, b in zipped_lines]
    return lines, n + m + u, max(p, q) + 2, n + u // 2


BST = BinarySearchTree(6)
BST.insert(3)
BST.insert(2)
BST.insert(4)
BST.insert(-1)
BST.insert(1)
BST.insert(-2)
BST.insert(8)
BST.insert(7)

print("before deletion:")
display(BST.root)

BST.delete(10)
print("after deletion:")
display(BST.root)


#Pre-Order Traversal
'''
In this traversal, the elements are traversed in “root-left-right” order. We first visit the root/parent node, then the left child, and then the right child. Here is a high-level description of the algorithm for Pre-Order traversal, starting from the root node:

    Visit the current node, i.e., print the value stored at the node

    Call the preOrderPrint() function on the left sub-tree of the ‘current Node’.

    Call the preOrderPrint() function on the right sub-tree of the ‘current Node’.

'''


def preOrderPrint(node):
    if node is not None:
        print(node.val)
        preOrderPrint(node.leftChild)
        preOrderPrint(node.rightChild)

BST = BinarySearchTree(6)
BST.insert(4)
BST.insert(9)
BST.insert(5)
BST.insert(2)
BST.insert(8)
BST.insert(12)

preOrderPrint(BST.root)

#First, we create an object of the BinarySearchTree class and insert some values into it. We will then pass the tree’s root to the preOrderPrint() function. If the node given is not None, this function prints the value at the node and calls preOrderPrint() on the left child first and then on the right child. Also note that we have hidden the Node class to make the code shorter! We have done the same for the next couple of chapters.
'''
This is a linear time algorithm, i.e., the time complexity of is in O(n)O(n)O(n) because a total of nnn recursive calls occur.

If you have understood Pre-Order Traversal clearly, it will be a piece of cake for you to understand the rest of the traversals, as all three of them are similar to one another. In the next lesson, we are going to study another type of BST Traversal known as Post-Order Traversal.
'''

#Post-Order Traversal
'''
In post-order traversal, the elements are traversed in “left-right-root” order. We first visit the left child, then the right child, and then finally the root/parent node. Here is a high-level description of the post-order traversal algorithm,

    Traverse the left sub-tree of the ‘currentNode’ recursively by calling the postOrderPrint() function on it.

    Traverse the right sub-tree of the ‘currentNode’ recursively by calling the postOrderPrint() function on it.

    Visit current node and print its value

'''
def postOrderPrint(node):
    if node is not None:
        postOrderPrint(node.leftChild)
        postOrderPrint(node.rightChild)
        print(node.val)


BST = BinarySearchTree(6)
BST.insert(4)
BST.insert(9)
BST.insert(5)
BST.insert(2)
BST.insert(8)
BST.insert(12)

postOrderPrint(BST.root)

#In-Order Traversal
'''
In In-order traversal, the elements are traversed in “left-root-right” order so they are traversed in order. In other words, elements are printed in sorted ascending order with this traversal. We first visit the left child, then the root/parent node, and then the right child. Here is a high-level description of the in-order traversal algorithm,

    Traverse the left sub-tree of the ‘currentNode’ recursively by calling the inOrderPrint() function on it.

    Visit the current node and print its value

    Traverse the right sub-tree of the ‘currentNode’ recursively by calling the inOrderPrint() function on it.

'''

def inOrderPrint(node):
    if node is not None:
        inOrderPrint(node.leftChild)
        print(node.val)
        inOrderPrint(node.rightChild)


BST = BinarySearchTree(6)
BST.insert(4)
BST.insert(9)
BST.insert(5)
BST.insert(2)
BST.insert(8)
BST.insert(12)

inOrderPrint(BST.root)
#AVL Tree?
'''
Adelson-Velsky and Landi in 1962, they claimed that AVL trees are “An algorithm for the organization of information.”
They are Binary Search Trees such that for every internal node vvv of the tree TTT, the heights of vvv's children can differ by at most 111. To put it simply, for each Node, the height of the left and right subtrees in an AVL tree can differ at most by one or the tree is balanced. If at any point their difference becomes more than one, steps are taken to re-balance the tree.

Time Complexity #

In case of binary search trees, the time complexity of all three basic operations, Insertion, Deletion, and Search, take O(h)O(h)O(h) time, where “h” is the height of the Binary Search Tree. The worst case time complexity is O(n)O(n)O(n), for skewed BSTs, where “n” is the number of nodes in the tree. This is the same as an array or list. However, in the best case, when the tree is completely balanced, the time complexity for basic operations is O(log(n))O(log(n))O(log(n)). AVL trees are essentially that: BSTs in the best-case.

The following diagram is an example of a valid AVL Tree
'''


'''
Insertion:

Insertion in AVL trees is done the same way that BST insertion is done. However, when a node is inserted into a BST it usually becomes unbalanced, i.e., the tree has a node which has a left-right subtree height difference greater than 1. So, AVL trees have to be rebalanced after insertion, unlike BSTs. To re-balance the tree, we need to perform a ‘rotation’. But before going deep let’s look at AVL tree rebalancing case-by-case.

Let’s look at terms that we will be using while re-balancing the tree.

Node U – an unbalanced node
Node C – child node of node U
Node G – grandchild node of node U

To rebalance the tree, we will perform rotations on the subtree with Node U being the root node. There are two types of rotations (left and right). We came across four different scenarios based on the arrangements of Nodes U, C, and G.

Left-Left: Node C is the left-child of Node U, and Node G is left-child of Node C

Left-Right: Node C is the left-child of Node U, and Node G is right-child of Node C

Right-Right: Node C is the right-child of Node U, and Node G is right-child of Node C

Right-Left: Node C is right-child of Node U, and Node G is left-child of Node C
'''

'''
Deletion

Algorithm for Deletion #

Here is a high-level description of the algorithm for deletion.
1. Delete the given node: #

Delete the given node in the same way as in BST deletion. At this point, the tree will become unbalanced and, to rebalance the tree, we would need to perform some kind of rotation (left or right). At first, we need to define the structure of AVL Tree and some nodes relative to the currentNode which is inserted using step one.
2. Traverse Upwards: #

Start traversing from the given node upwards till you find the first unbalanced node. Let’s look at some of the terms which we will be using while re-balancing the tree.

    Node U — an unbalanced node
    Node C — child node of node U
    Node G — grandchild node of node U

3. Rebalance the Tree #

In order to rebalance the tree, we will perform rotations on the subtree where U is the root node. There are two types of rotations (left, right). We came across four different scenarios based on the arrangements of Nodes U, C and, G.

    Left-Left: Node C is the left-child of Node U, and Node G is left-child of Node C

    Left-Right: Node C is the left-child of Node U, and Node G is right-child of Node C

    Right-Right: Node C is the right-child of Node U, and Node G is right-child of Node C

    Right-Left: Node C is right-child of Node U, and Node G is left-child of Node C

After performing successful rotation for the first unbalanced Node U, traverse up and find the next un-balanced Node and perform the same series of operations to balance. Keep on balancing the unbalanced nodes from first Node U to ancestors of Node U until we reach the root. After that point, we will have a fully balanced AVL Tree that follows its property.
'''

#Red-Black Tree
'''
Red-Black Trees are another type of self-balancing Binary Search Tree, but with some additions: the nodes in Red-Black Trees are colored either red or black. Colored nodes help with re-balancing the tree after insertions or deletions.



    Every node is either Red or Black in color

    The root is always colored Black

    Two Red nodes cannot be adjacent, i.e., No red parent can have a red child and vice versa

    Each path from the root to None contains the same number of Black colored nodes

    The color of None nodes is considered Black

Time Complexity #

Balancing the tree doesn’t result in a tree being perfectly balanced, but it is good enough to make time complexity of basic operations like searching, deletion, and insertion to be around O(logn).

'''
class Node:
  def __init__(self,val):
    self.val = val
    self.leftChild = None
    self.rightChild = None
    isRed = None # True if Node is RedColored else false

'''
Although AVL Trees are technically more ‘balanced’ than Red-Black Trees, AVL Trees take more rotations during insertion and deletion operations than Red-Black Trees. So, if you have search-intensive applications where insertion and deletion are not that frequent, use AVL Trees, otherwise, use Red-Black Trees.

Insertion:
Insertion in Red-Black Tree #

Here is a high-level description of the algorithm involved in inserting a value in a Red-Black Tree:

    Insert the given node using the standard BST Insertion technique that we studied earlier and color it Red.

    If the given node is the root, then change its color to Black

    If the given node is not the root, then we will have to perform some operations to make the tree follow the Red-Black property.

Rebalancing the Tree #

There are two ways to balance an unbalanced tree:

    Recoloring Nodes
    Rotating Nodes (left or right)

But before the details are explained, let’s define the structure of the Red-Black Tree and some nodes relative to the given node, which is the node that we inserted in the Tree.

    Node C – the newly inserted node
    Node P – the parent of the newly inserted node
    Node G – the grandparent of the newly inserted node
    Node U – the sibling of the parent of the newly inserted node, i.e., the sibling of Node P / child of Node G

If the newly inserted node is not a root and the parent of the newly inserted node is not Black, first, we will check Node U and based on Node U’s color, we balance the tree. If Node U is Red, do the following:

    Change color of Node P and U to Black
    Change color of Node G to Red
    Make Node G the new currentNode and repeat the same process from step two
If Node U is Black, then we come across four different scenarios based on the arrangements of Node P and G, just like we did in AVL trees. We will cover each of these scenarios and try to help you understand through illustrations.

    Left-Left: Node P is the leftChild of Node G and currentNode is the leftChild of Node P

    Left-Right: Node P is the leftChild of Node G and currentNode is the rightChild of Node P

    Right-Right: Node P is the rightChild of Node G and currentNode is the rightChild of Node P

    Right-Left: Node P is the rightChild of Node G and currentNode is the leftChild of Node P

Case 1: Left-Left #

In case when the Node P is the leftChild of Node G and currentNode is the leftChild of Node P, we perform the following steps. Look at the illustration below for a better understanding.

    Right Rotate Node G
    Swap the colors of Nodes G and P

Case 2: Left-Right #

In the case when the Node P is the leftChild of Node G and the currentNode is the rightChild of Node P, we perform the following steps. Look at the illustration below for better understanding:

    Left Rotate Node P
    After that, repeat the steps that we covered in the Left-Left case

Case 3: Right-Right #

In the case when Node P is the rightChild of Node G and the currentNode is the rightChild of Node P, we perform the following steps. Look at the illustration below for a better understanding.

    Left Rotate Node G
    Swap colors of Node G and P
Case 4: Right-Left #

In the case when Node P is the rightChild of Node G and the currentNode is the leftChild of Node P, we perform the following steps. Look at the illustration below for a better understanding.

    Right Rotate Node P
    After that, repeat the steps that we covered in Right-Right case

'''

'''
Deletion

In insertion, we may violate the alternating parent-child color property, i.e., a red parent may have a red child. But in the deletion function, we may end up deleting a black node that could violate the property that “the same number of black nodes must exist from the root to the None node for every path.”

In insertion, we check the color of the sibling of the parent of the currentNode and based on the color we perform appropriate operations to balance the tree. But now in the deletion operation, we will check the color of the sibling node of the currentNode and based on its color, we will perform some actions to balance the tree again.

Here is a high-level description of the algorithm to remove a value in a Red-Black Tree:

    Search for a node with the given value to remove. We will call it currentNode
    Remove the currentNode using the standard BST deletion operation that we studied earlier

When deleting in a BST, we always end up deleting either a leaf node or a node with only one child because if we want to delete an internal node, we always swap it with a leaf node or a node with at most one child.

    In case of the leaf node deletion, delete the node and make the child of the parent of the node to be deleted None
    In case of a node with one child only, link the parent of the node to be deleted with that one child.

Let’s name some nodes relative to Node C, which is the node that we want to delete:

    Node C – The node to be deleted (let’s call it currentNode)
    Node P – The parent node of the currentNode
    Node S – The sibling node (once we rotate the tree, Node R will have a sibling node which we name Node S)
    Node SC – The child node of Node S
    Node R – The node to be Replaced with the currentNode and linked with Node P (Node R is the single child of Node C)

Deletion Cases #

Let’s study the deletion cases and the steps performed in each of these cases to make the tree balanced again. Given below is the first case in which Node C or Node R is red. In this type of scenario, we make Node R black and link it to Node P

The second case is if both Node C and Node R are black, then make Node R black. Now Node R is double black, i.e., it was already black and, when we found both Node C and Node R black, then we again make Node R black. Remember that “None” node is always black. Let’s now convert Node R from double to single black.

We need to perform the following steps while Node R is double black and it is not the root of the Tree. If Node S (sibling of Node R) is Black and one or both of Node S children are Red:

    Left-Left: Node S is leftChild of Node P and Node SC (red) is leftChild of S, or both children of S are red

    Right-Right: Node S is rightChild of Node P and Node SC (red) is rightChild of S, or both children of S are red

    Left-Right: Node S is leftChild of Node P and Node SC (red) is rightChild of S

    Right-Left: Node S is rightChild of Node P and Node SC (red) is leftChild of S

Case 1: Left-Left #

In case the Node S is leftChild of Node P and Node SC (red) is leftChild of S, or both children of S are red, we perform the following steps. Look at the illustration below for better understanding:

    Rotate Node P towards right
    Make right child of Node S the left child of Node P

Case 2: Right-Right #

In case the Node S is rightChild of Node P and Node SC (red) is rightChild of S, or both children of S are red, we perform the following steps. Look at the illustration below for better understanding:

    Rotate Node P towards left
    Make left child of Node S the right child of Node P

Case 3: Left-Right #

In case the Node S is leftChild of Node P and Node SC (red) is rightChild of S, we perform the following steps. Look at the illustration below for better understanding:

    Rotate Node S towards left
    Rotate Node P towards right
Case 4: Right-Left #

In case the Node S is rightChild of Node P and Node SC (red) is leftChild of S, we perform the following steps. Look at the illustration below for better understanding:

    Rotate Node S towards right
    Rotate Node P towards left



'''

'''
A 2-3 Tree(O [log n]) is another form of search tree, but is very different from a Binary Search Tree. Unlike BST, 2-3 Tree is a balanced and ordered search tree which provides a very efficient storage mechanism to guarantee fast operations. In this chapter, we will take a detailed look at 2-3 Trees’ structure, the limitations it follows, and how elements are inserted and deleted from it.

One key feature of a 2-3 Tree is that it remains balanced, no matter how many insertions or deletion you perform. The leaf nodes are always present on the same level and are quite small in number. This is to make sure the height doesn’t increase up to a certain level as the time complexity of all the operations is mainly dependent upon it. Ideally, we want the height to be in logarithmic terms because as the tree grows larger it will require more time to perform operations. In 2-3 Trees, the height is logarithmic in the number of nodes present in the tree. They generally come in 2 forms:

    2 Node Tree
    3 Node Tree

See the figures below to get the idea of how they are different. Given below is a 2-3 Tree with only two nodes. To keep it ordered, the left child key must be smaller than the parent node key. Similarly, right child key must be greater than the parent key.
The figure below shows a 3-node tree where each node can contain two keys and three children at max. Here, parent node has 2 keys and 3 children which are all at the same level. Let’s say the first key at parent node is X and we call the second one Y. As shown in the figure, X key is greater than the left child and Y key is smaller than the child key at right. The middle child has the value that is greater than X and smaller than Y.

Concluding from the explanation above, 2-3 Trees acquire a certain set of properties to keep the structure balanced and ordered. Let’s take a look at these properties.
Properties: #

    All leaves are at the same height.

    Each internal node can either have 2 or 3 children.

    If the node has one key, it can either be a leaf node or has exactly two children. Let’s say X is the key and LChild, and RChild refers to the left and right child of the node respectively, then:

LChild.Key<X<RChild.KeyLChild.Key < X < RChild.Key LChild.Key<X<RChild.Key

    If the node has two keys, it can either be a leaf node or has exactly three children. Let’s say X, and Y are the keys present at a node and LChild and RChild refer to the left and right child of the node respectively then:

LChild.Key<X<MChild.Key<Y<RChild.KeyLChild.Key < X < MChild.Key < Y < RChild.Key LChild.Key<X<MChild.Key<Y<RChild.Key

    Finally, the height of a 2-3 Tree with n number of nodes will always be lesser than:

log2(n+1)log_2(n+1) log​2​​(n+1)

'''
'''
Insertion

In 2-3 Trees, values are only inserted at leaf nodes based on certain conditions. As discussed before, the insertion algorithm takes O(Logn)O(Logn)O(Logn) time where n is the number of nodes in the tree. Searching an element is done in Log(n)Log(n)Log(n) and then insertion takes a constant amount of time. So overall the time complexity of insertion algorithm is O(Logn)O(Logn)O(Logn). Let’s see how it works.
Insertion Algorithm: #

The insertion algorithm is based on these scenarios:

    Initially if the tree is empty, create a new leaf node and insert your value
    If the tree is not empty, traverse through the tree to find the right leaf node where the value should be inserted
    If the leaf node has only one value, insert your value into the node
    If the leaf node has more than two values, split the node by moving the middle element to the top node
    Keep forming new nodes wherever you get more than two elements


Deletion
Case 1: Element at Leaf: #

When the element which needs to be removed is present at the leaf node, we check how many keys are present in that node; this further divides the algorithm into two scenarios:
1.1 Leaf node has more than one key: #

If the leaf at which the element to be deleted has more than one key, then simply delete the element.

1.2 Leaf node only has one key: #

If the leaf node where the element to be removed is present has only one key, then we will have to adjust the keys of that sub-tree in such a way that it remains ordered and balanced. This condition is further divided into two scenarios:

1.2.1 Any of the siblings has two keys: #

Siblings mean the other adjacent leaf nodes that share the same parent. A node could have one or two siblings depending upon its position. Check how many keys are present at left or right sibling nodes. If any of the siblings have more than one key, then your problem is solved. All you need to do is move an element from the sibling node to the parent node and shift down a node from parent to your node. This process is called Redistribution by Rotation and it can be performed in two ways:

Rotation from Left Sibling: #

In this case, we lend a key from left sibling by shifting up the key having largest value in the node to parent node and move down parent node key (most right) to our node.
Rotation from Right Sibling: #

In this case, we lend a key from right sibling by shifting up the key having smallest value in the node to parent node and move down parent node key (most left) to our node.

1.2.2 No sibling has more than one key: #

    In the case when none of the siblings have more than one key, we have no other option but to merge the two nodes by rotation of key. So we merge two child nodes into one node by rotating elements accordingly. This process is called Merge by Rotation.

    If child nodes have more than one keys, we shift an element from the child node to make it the parent node. When we are left with only one key at each child node, then we are bound to delete the node.

Case 2: Element at Internal Node: #

Deletion is always performed at the leaf. So whenever we need to delete a key at the internal node, we swap it with any of its in-order successors and somehow make it shift to any leaf node as deletion is always performed at the leaf. Shift the element at the leaf node and then delete it. The element to be deleted can be swapped by:

    an element with the largest key on the left
    an element with the smallest key on the right

This is applicable when the child node has more than one key stored at the node. If there is only one value at child node, then you are bound to swap the parent with whatever value child node has.


'''

'''
2-3-4 is a search tree which is an advanced version of 2-3 Trees. This tree can accommodate more keys and hence more child nodes as compared to 2-3 Trees. 2-3-4 satisfies all the properties covered in 2-3 Trees along with some additional key features:

    Each internal node can contain at max three keys

    Each internal node can have at max four child nodes

    In case of three keys at an internal node namely left, mid, and right key, all the keys present at LeftChild node are smaller than the left key, which can be mathematically expressed as:

LeftChild.keys<LeftKeyLeftChild.keys < LeftKey LeftChild.keys<LeftKey

    All the keys present at LeftMidChild node are smaller than the mid key, which can be mathematically expressed as:

LeftMidChild.keys<MidKeyLeftMidChild.keys < MidKey LeftMidChild.keys<MidKey

    All the keys present at RightMidChild node are smaller than the right key, which can be mathematically expressed as:

RightMidChild.keys<RightKeyRightMidChild.keys < RightKey RightMidChild.keys<RightKey

    Finally, all the keys present at RightChild node are greater than the right key, which can be mathematically expressed as:

RightChild.keys>RightKeyRightChild.keys > RightKey RightChild.keys>RightKey
'''

'''
Challenge 1: Find minimum value in Binary Search Tree
This solution first checks if the given root is None and returns None if it is. Then, it moves on to the left sub-tree and keeps going to each node’s left child until the left-most child is found.
Time Complexity #

The time complexity of this solution is in O(h)O(h)O(h). In the worst case, the BST will be left skewed and the height will be nnn and so the time complexity will be O(n).
'''
def findMin(root):
    if root is None:  # check for None
        return None
    while root.leftChild:  # Traverse until the last child
        root = root.leftChild
    return root.val  # return the last child

def findMin(root):
    if root is None:  # check if root exists
        return None
    elif root.leftChild is None:  # check if left child exists
        return root.val  # return if not left child
    else:
        return findMin(root.leftChild)  # recurse onto the left child
BST = BinarySearchTree(6)
BST.insert(20)
BST.insert(-1)

print(findMin(BST.root))

'''
Challenge 2: Find kth maximum value in Binary Search Tree
This is a quick and easy naive solution for this problem. In this solution, to find the kth max value, we first perform an In-Order Traversal on the tree to get a sorted array in ascending order. Before appending to the list, we cross-check with the last element for equality to avoid duplicates. Once, we have the sorted array, we can easily find the kth max. value by accessing the index [length - k]. To perform the in-order traversal on the tree,​ we use a helper recursive function which is a variation of the inOrderPrint() function that we studied in the in-Order Traversal.
Time Complexity #

The worst-case and the best-case complexity of this solution is O(n)O(n)O(n) where nnn is the number of nodes in the tree. The reason is that no matter the value of k is, the function always traverses the entire tree!

The recursive approach is more efficient than the previous solution. In this solution, we have used a helper function called findkthMaxRecursive() and the function findKthMax() acts as a wrapper for this helper function. In the recursive function we first recursively traverse the tree in a right to left fashion because the maximum element is present in the right-most leaf node. We have also kept a global variable called counter which gets incremented after we have found the maximum element and current_max variable to track the previous value. The counter is incremented each time if kth maximum node is not found and the node value is not current_max to cater to duplicates. The base condition is reached when k becomes equal to the counter. This node is then returned to the wrapper function, and if the node is not None, then its value is returned.
Time Complexity #

The worst-case complexity of this solution is the same as the previous solution, i.e O(n)O(n)O(n). But for the best-case scenario, when k = 1, the complexity of this solution will be O(h)O(h)O(h) where hhh is the height of the tree. Therefore, on average, this solution is more efficient than the previous one.
'''
def findKthMax(root, k):
    tree = []
    inOrderTraverse(root, tree)  # Get sorted tree list
    if ((len(tree)-k) >= 0) and (k > 0):  # check if k is valid
        return tree[-k]  # return the kth max value
    return None  # return none if no value found


def inOrderTraverse(node, tree):
    # Helper recursive function to traverse the tree inorder
    if node is not None:  # check if node exists
        inOrderTraverse(node.leftChild, tree)  # traverse left sub-tree
        if len(tree) is 0:
            # Append if empty tree
            tree.append(node.val)
        elif tree[-1] is not node.val:
            # Ensure not a duplicate
            tree.append(node.val)  # add current node value
        inOrderTraverse(node.rightChild, tree)

def findKthMax(root, k):
    if k < 1:
        return None
    node = findKthMaxRecursive(root, k)  # get the node at kth position
    if(node is not None):  # check if node received
        return node.val  # return kth node value
    return None  # return None if no node found


counter = 0  # global count variable
current_max = None

def findKthMaxRecursive(root, k):
    global counter  # use global counter to track k
    global current_max # track current max
    if(root is None):  # check if root exists
        return None

    # recurse to right for max node
    node = findKthMaxRecursive(root.rightChild, k)
    if(counter is not k) and (root.val is not current_max):
        # Increment counter if kth element is not found
        counter += 1
        current_max = root.val
        node = root
    elif current_max is None:
        # Increment counter if kth element is not found
        # and there is no current_max set
        counter += 1
        current_max = root.val
        node = root
    # Base condition reached as kth largest is found
    if(counter == k):
        return node  # return kth node
    else:
        # Traverse left child if kth element is not reached
        # traverse left tree for kth node
        return findKthMaxRecursive(root.leftChild, k)

'''
Challenge 3: Find Ancestors of a given node in a BST
This solution uses a recursive helper function that The recursive function starts traversing from the root till the input node and backtracks to append the ancestors that led to the node.
Time Complexity #

This is an O(n)O(n)O(n) time function since it iterates over all of the nodes of the entire tree.

The iterative solution conducts a search for k in the BST until a None node or k itself is reached. If k is reached, the ancestors are returned, otherwise, an empty list is returned.
Time Complexity #

The time complexity of this solution is O(log(n))O(log(n))O(log(n)) since a path from the root to k is traced.


'''
def findAncestors(root, k):
    result = []
    recfindAncestors(root, k, result)  # recursively find ancestors
    return str(result)  # return a string of ancestors


def recfindAncestors(root, k, result):
    if root is None:  # check if root exists
        return False
    elif root.val is k:  # check if val is k
        return True
    recur_left = recfindAncestors(root.leftChild, k, result)
    recur_right = recfindAncestors(root.rightChild, k, result)
    if recur_left or recur_right:
        # if recursive find in either left or right sub tree
        # append root value and return true
        result.append(root.val)
        return True
    return False  # return false if all failed


def findAncestors(root, k):
    if not root:  # check if root exists
        return None
    ancestors = []  # empty list of ancestors
    current = root  # iterator current set to root

    while current is not None:  # iterate until we reach None
        if k > current.val:  # go right
            ancestors.append(current.val)
            current = current.rightChild
        elif k < current.val:  # go left
            ancestors.append(current.val)
            current = current.leftChild
        else:  # when k == current.val
            return ancestors[::-1]
    return []

'''
Challenge 4: Find the Height of a BST

Here, we return -1 if the given node is None. Then, we call the findHeight() function on the left and right subtrees and return the one that has a greater value plus 1. We will not return 0 if the given node is None as the leaf node will have a height of 0.
Time Complexity #

The time complexity of the code is O(n)O(n)O(n) as all the nodes of the entire tree have to be traversed.
'''
def findHeight(root):
    if root is None:  # check if root exists
        return -1  # no root means -1 height
    else:
        max_sub_tree_height = max(
            findHeight(root.leftChild),
            findHeight(root.rightChild)
        )  # find the max height of the two sub-tree
        # add 1 to max height and return
        return 1 + max_sub_tree_height


BST = BinarySearchTree(6)
BST.insert(4)
BST.insert(9)
BST.insert(5)
BST.insert(2)
BST.insert(8)
BST.insert(12)
BST.insert(10)
BST.insert(14)


print(findHeight(BST.root))

'''
Challenge 5: Find Nodes at "k" distance from the Root

Sample Input #

bst = {
    6 -> 4,9
    4 -> 2,5
    9 -> 8,12
    12 -> 10,14
}
where parent -> leftChild,rightChild
k = 2

o/p = [2,5,8,12]

This solution maintains a counter k that is decremented until it is 0 or a leaf node is reached, returning the nodes that are encountered at k == 0
Time Complexity #

The time complexity of this solution is in O(n)O(n)O(n)

'''
def findKNodes(root, k):
    res = []
    findK(root, k, res)  # recurse the tree for node at k distance
    return str(res)


def findK(root, k, res):
    if root is None:  # return if root does not exist
        return
    if k == 0:
        res.append(root.val)  # append as root is kth node
    else:
        # check recursively in both sub-tree for kth node
        findK(root.leftChild, k - 1, res)
        findK(root.rightChild, k - 1, res)


BST = BinarySearchTree(6)
BST.insert(4)
BST.insert(9)
BST.insert(5)
BST.insert(2)
BST.insert(8)
BST.insert(12)
print(findKNodes(BST.root, 2))