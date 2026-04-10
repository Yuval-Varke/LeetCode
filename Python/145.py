# 145. Binary Tree Postorder Traversal

# Given the root of a binary tree, return the postorder traversal of its nodes' values.

 

# Example 1:
# [https://assets.leetcode.com/uploads/2024/08/29/screenshot-2024-08-29-202743.png]
# Input: root = [1,null,2,3]

# Output: [3,2,1]

# Explanation:



# Example 2:
# [https://assets.leetcode.com/uploads/2024/08/29/tree_2.png]
# Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

# Output: [4,6,7,5,2,9,8,3,1]

# Explanation:



# Example 3:

# Input: root = []

# Output: []

# Example 4:

# Input: root = [1]

# Output: [1]

 

# Constraints:

# The number of the nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100





# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def postorder(root):
            if not root:
                return
            postorder(root.left)
            postorder(root.right)
            ans.append(root.val)
        postorder(root)
        return ans