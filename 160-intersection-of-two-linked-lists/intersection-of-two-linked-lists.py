# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        nodesA, nodesB = [], []

        def traversal(head, arr):
            curr = head
            while curr:
                arr.append(curr)  
                curr = curr.next

        traversal(headA, nodesA)
        traversal(headB, nodesB)

        
        intersection = None
        i, j = len(nodesA) - 1, len(nodesB) - 1
        while i >= 0 and j >= 0 and nodesA[i] == nodesB[j]:
            intersection = nodesA[i]
            i -= 1
            j -= 1

        
        return intersection