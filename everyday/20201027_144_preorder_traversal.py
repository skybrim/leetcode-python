"""
144. 二叉树的前序遍历

给定一个二叉树，返回它的 前序 遍历。
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val;
        self.left = left
        self.right = right


def recursive_preorder_traversal(root):
    """
    递归
    """
    result = []

    def recursive_order(node):
        if node == None:
            return
        result.append(node.val)
        recursive_order(node.left)
        recursive_order(node.right)

    recursive_order(root)
    return result


def iteration_preorder_traversal(root):
    result = []
    if root == None:
        return result
    stack = [root]
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.right != None:
            stack.append(node.right)
        if node.left != None:
            stack.append(node.left)
    return result
