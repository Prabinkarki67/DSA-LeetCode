# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def symmetric_check(lft, rt):
            if not lft and not rt:
                return True
            if not lft or not rt:
                return False
            return (lft.val==rt.val and symmetric_check(lft.left, rt.right)and symmetric_check(lft.right, rt.left))
        return symmetric_check(root.left, root.right)