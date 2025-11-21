# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def preTraversal(node, res):
            if node is None:
                return
            res.append(node.val)
            preTraversal(node.left, res)
            preTraversal(node.right, res)
        res=[]
        preTraversal(root, res)
        return res