# BinaryBreadthFirst.py
# author: William Pulkownik
# description: Given the root of a binary tree, return the level order
# traversal of the node values (left to right, top to bottom)

####################################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
####################################
from typing import Deque, no_type_check_decorator


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        to_visit = Deque([root] if root else [])
        
        while len(to_visit):
            level = []
            length = len(to_visit)
            for i in range(length):
                node = to_visit.popleft()
                level.append(node.val)
                if node.left:
                    to_visit.append(node.left)
                if node.right:
                    to_visit.append(node.right)
            result.append(level)
        return result
        