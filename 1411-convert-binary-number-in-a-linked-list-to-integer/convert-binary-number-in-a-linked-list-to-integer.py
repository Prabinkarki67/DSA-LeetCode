# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        def trav(head):
            sum=[]
            curr=head
            while curr:
                sum.append(curr.val)
                curr=curr.next
            return sum
        #fetch the value and form list
        num=trav(head)
        #conv to binary
        n=len(num)
        bina=0
        for i in range(n):
            powr=n-1-i
            bina=bina+num[i]*(2**powr)
        return bina