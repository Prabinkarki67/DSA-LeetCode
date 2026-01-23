# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], target: int) -> bool:


        ##my thinking:: first do travelsal doing add to all leaf node and form list and see if that list has target
        ans = []
        add = 0
        def fill_ans(root, ans, add):
            if root is None:
                return 
                
            add += root.val


            if root.left is None and root.right is None:  #leafnode
                ans.append(add)
                return

            fill_ans(root.left, ans, add)
            fill_ans(root.right, ans, add)
        

        fill_ans(root, ans, add)
        if target in ans:
            return True
        return False