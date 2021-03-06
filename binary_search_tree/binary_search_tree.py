import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


# Binary Search Tree - discards duplicate values
class BinarySearchTree:
    def __init__(self, value, parent=None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent

    # Insert the given value into the tree
    def insert(self, value):
        newNode = None
        if value < self.value:
            if self.left:
                newNode = self.left.insert(value)
            else:
                newNode = BinarySearchTree(value, self)
                self.left = newNode
        elif value > self.value:
            if self.right:
                newNode = self.right.insert(value)
            else:
                newNode = BinarySearchTree(value, self)
                self.right = newNode
        return newNode

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        else:
            if target < self.value:
                if self.left:
                    return self.left.contains(target)
                else:
                    return False
            else:
                if self.right:
                    return self.right.contains(target)
                else:
                    return False

    # Return the maximum value found in the tree
    def get_max(self):
        return self.__getMaxNode().value

    def __getMaxNode(self):
        theMax = self
        if self.right:
            theMax = self.right.__getMaxNode()
        return theMax

    # Return the minimum value found in the tree
    def get_min(self):
        return self.__getMinNode().value

    def __getMinNode(self):
        theMin = self
        if self.left:
            theMin = self.left.__getMinNode()
        return theMin

    # 2) If right sbtree of node is NULL, then succ is one of the ancestors. Do following.
    # Travel up using the parent pointer until you see a node which is the left child of its parent. The parent of such a node is the succ.
    def getInorderSuccessor(self):
        node = self.__getInorderSuccessorNode()
        if node:
            return node.value
        else:
            return None

    def __getInorderSuccessorNode(self):
        if self.right:
            return self.right.__getMinNode()
        else:
            current = self
            parent = current.parent
            while current is not None and parent is not None and current != parent.left:
                parent = parent.parent
                current = current.parent
            return parent

    # 2) If left sbtree of node is NULL, then pred is one of the ancestors. Do following.
    # Travel up using the parent pointer until you see a node which is the right child of its parent. The parent of such a node is the pred.
    def getInorderPredecessor(self):
        node = self.__getInorderPredecessorNode()
        if node:
            return node.value
        else:
            return None

    def __getInorderPredecessorNode(self):
        if self.left:
            return self.left.__getMaxNode()
        else:
            current = self
            parent = current.parent
            while current is not None and parent is not None and current != parent.right:
                parent = parent.parent
                current = current.parent
            return parent

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.right:
            self.right.for_each(cb)
        if self.left:
            self.left.for_each(cb)

    def delete(self, value, parent=None):
        # find node if it exists
        node = self
        while node is not None and node.value != value:
            if node.value > value:
                node = node.left
            else:
                node = node.right
        if node is None:
            return
        node.__deleteSelf()

    def __deleteSelf(self):
        # if node has two children, find inorder successor, delete it, and copy its value here
        # if it has one child, move child in place of node
        # if has no children, delete
        if self.left is not None and self.right is not None:
            successor = self.__getInorderSuccessorNode()
            self.value = successor.value
            successor.__deleteSelf()
        elif self.left or self.right:
            child = self.left or self.right
            if self.parent.left == self:
                self.parent.left = child
            else:
                self.parent.right = child
            child.parent = self.parent
        elif self.left is None and self.right is None:
            parent = self.parent
            if parent.left == self:
                parent.left = None
            else:
                parent.right = None
            self.parent = None

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # # cleaner, but requires additions like getting in order successor and utilizing nodes internally
        # node = self.__getMinNode()
        # while node:
        #     print(node.value)
        #     node = node.__getInorderSuccessorNode()

        # works, doesn't require the additions, but not as elegent- really quirky with parameter passing
        if self.left:
            self.left.in_order_print(None)
        print(self.value)
        if self.right:
            self.right.in_order_print(None)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        theQueue = Queue()

        currentNode = node
        while currentNode:
            print(currentNode.value)
            if currentNode.left:
                theQueue.enqueue(currentNode.left)
            if currentNode.right:
                theQueue.enqueue(currentNode.right)
            currentNode = theQueue.dequeue()

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        theStack = Stack()

        currentNode = node
        while currentNode:
            print(currentNode.value)
            if currentNode.right:
                theStack.push(currentNode.right)
            if currentNode.left:
                theStack.push(currentNode.left)
            currentNode = theStack.pop()

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        print(self.value)
        if self.left:
            self.left.pre_order_dft(None)
        if self.right:
            self.right.pre_order_dft(None)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if self.left:
            self.left.post_order_dft(None)
        if self.right:
            self.right.post_order_dft(None)
        print(self.value)
