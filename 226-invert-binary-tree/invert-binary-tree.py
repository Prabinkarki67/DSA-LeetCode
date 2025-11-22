# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def form_tree(node):
            if node is None:
                return 
            left = node.left
            right = node.right

            node.left = right
            node.right = left

            form_tree(node.left)
            form_tree(node.right)

        form_tree(root)
        return root
        