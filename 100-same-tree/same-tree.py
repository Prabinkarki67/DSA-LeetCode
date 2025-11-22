# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def tree_checker(p, q):
            if p is None and q is None:  # both empty → same
                return True

            if p is None or q is None:   # one empty → not same
                return False

            if p.val != q.val:
                return False
            
            return tree_checker(p.left, q.left) and tree_checker(p.right, q.right)


        return tree_checker(p, q)
        