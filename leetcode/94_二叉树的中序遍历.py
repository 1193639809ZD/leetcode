#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inOrder(node):
            if node:
                if node.left:
                    inOrder(node.left)
                ans.append(node.val)
                if node.right:
                    inOrder(node.right)
            else:
                return

        ans = []
        inOrder(root)
        return ans


# @lc code=end
