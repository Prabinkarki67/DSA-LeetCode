# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        def fill_elem(node, elem):
            if node is None:
                return


            #left -> root -> right
            
            fill_elem(node.left, elem)
            elem.append(node.val)
            fill_elem(node.right, elem)

        elem = []
        fill_elem(root, elem)
        return elem
        