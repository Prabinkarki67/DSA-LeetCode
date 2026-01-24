# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        path = []
        def trav(root, val):
            if root is None:
                return
            val += str(root.val)
            if root.left is None and root.right is None:
                path.append(val)
            
            trav(root.left, val + "->")
            trav(root.right, val + "->")
        trav(root, '')
        return path