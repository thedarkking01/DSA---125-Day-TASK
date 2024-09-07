from sys import *
from collections import *
from math import *

# Following is the Binary Tree node structure:
class BinaryTreeNode :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None

def getTreeTraversal(root):
    # Write your code here.
    inorder = []
    preorder = []
    postorder = []

    def inorderTraversal(node):
        if not node:
            return
        inorderTraversal(node.left)
        inorder.append(node.data)
        inorderTraversal(node.right)

    def preorderTraversal(node):
        if not node:
            return
        preorder.append(node.data)
        preorderTraversal(node.left)
        preorderTraversal(node.right)

    def postorderTraversal(node):
        if not node:
            return
        postorderTraversal(node.left)
        postorderTraversal(node.right)
        postorder.append(node.data)
    inorderTraversal(root)
    preorderTraversal(root)
    postorderTraversal(root)
    return [inorder, preorder, postorder]