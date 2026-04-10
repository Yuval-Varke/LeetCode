# 110. Balanced Binary Tree

# Given a binary tree, determine if it is height-balanced.

 

# Example 1:
# [https://assets.leetcode.com/uploads/2020/10/06/balance_1.jpg]

# Input: root = [3,9,20,null,null,15,7]
# Output: true


# Example 2:
# [https://assets.leetcode.com/uploads/2020/10/06/balance_2.jpg]

# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
# Example 3:

# Input: root = []
# Output: true
 

# Constraints:

# The number of nodes in the tree is in the range [0, 5000].
# -104 <= Node.val <= 104





# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True
        def dfs(root):
            nonlocal res 
            if not root:
                return 0
            l = dfs(root.left)
            r = dfs(root.right)
            if abs(l-r) > 1:
                res = False
            return 1 + max(l,r)
        dfs(root)
        return res