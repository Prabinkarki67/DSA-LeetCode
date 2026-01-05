# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def merger(a,b):
            if not a:
                return b
            if not b:
                return a
            root = TreeNode(a.val+b.val)
            root.left = merger(a.left, b.left)
            root.right = merger(a.right, b.right)
            return root
        return merger(root1, root2)