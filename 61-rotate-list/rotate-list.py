# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        #find len of list
        length = 1
        curr = head
        while curr.next:
            curr = curr.next
            length += 1
        
        #make circular linked list
        curr.next = head

        #find the index of element just front of kth element from end
        new_indx = length - (k % length) - 1

        #traverse to the kth element
        curr = head
        for _ in range(new_indx):
            curr = curr.next
        
        #make the pointer head
        new_head = curr.next

        curr.next = None  # Break the circle
        
        return new_head