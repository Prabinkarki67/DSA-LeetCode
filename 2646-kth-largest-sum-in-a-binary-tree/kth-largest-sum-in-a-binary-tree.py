# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        def elemFiller(node, level, elem):
            if node is None:
                return
            if len(elem) <= level:
                elem.append([])
            elem[level].append(node.val)
            elemFiller(node.left, level+1, elem)
            elemFiller(node.right, level+1, elem)
        
        level = 0
        elem = []
        elemFiller(root, level, elem)
        res=[]
        for i in elem:
            res.append(sum(i))
        res.sort()
        if k > len(res):
            return -1
        return res[-k]
