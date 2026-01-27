# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #first find no of nodes
        def trav(head):
            curr=head
            counter = 0
            while curr:
                counter+=1
                curr=curr.next
            return counter
        count = trav(head)

        #return node after middle node
        def res(head, counter):
            curr=head
            indx=1
            while curr:
                if counter ==indx:
                    return curr
                indx+=1
                curr=curr.next
        
        if count%2!=0:  #odd
            n= (count+1)//2
        else:           #even
            n=(count+2)//2
        
        return res(head, n)
