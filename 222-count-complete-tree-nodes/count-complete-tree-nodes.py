# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def collect_element(node, element):
            if node is None:
                return
            element.append(node.val)
            collect_element(node.left, element)
            collect_element(node.right, element)
            
        element = []
        collect_element(root, element)
        return len(element)
