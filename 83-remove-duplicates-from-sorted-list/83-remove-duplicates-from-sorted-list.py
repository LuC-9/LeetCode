# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cNode=head
        if cNode == None:
            return
        nNode=cNode.next
        
        while cNode.next!=None:
            if  cNode.next.val==cNode.val:
                nNode=cNode.next.next
                cNode.next=nNode
            else:
                cNode=cNode.next
        return head
        