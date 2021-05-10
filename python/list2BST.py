# list2BST.py
# william pulkownik
# Given the head of a singly linked list where elements are sorted in ascending order, 
# convert it to a height balanced BST.

# For this problem, a height-balanced binary tree is defined as a binary tree in which 
# the depth of the two subtrees of every node never differ by more than 1.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


'''
In an attempt to get this done in O(n) time I will use the following method:
1) count nodes in the linked list
2) recursively construct left subtree with the left n/2 ListNodes
3) assign root and link left subtree
4) construct right subtree recursively and link to root
'''
class Solution:
    def countList(self, head):
        # make a count of the list nodes
        count = 0
        temp = head 
        while(temp != None): 
            temp = temp.next
            count = count + 1
        return count
    
    def makeTree(self, n):
        if (n <= 0):
            return None
        left = self.makeTree(int(n/2))
        root = TreeNode(self.temp.val)
        self.temp = self.temp.next
        root.left = left

        root.right = self.makeTree(n-int(n/2)-1)
        return root


    def sortedListToBST(self, head):
        self.temp = head
        if head == None:
            return None
        
        n = self.countList(head)
        if n == 1:
            return TreeNode(head.val)
        return self.makeTree(n)
