# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def mergeLists(head1, head2):
    
    temp = None
    
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    
    if head1.val <= head2.val:
        temp = head1
        temp.next = mergeLists(head1.next, head2)
    else:
        temp = head2
        temp.next = mergeLists(head1, head2.next)
        
    return temp




class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        #myList = ListNode(5)
        #myList.val = l1.val
        #print(myList.val)
        
        #print(l1.next.next.next)
      
        myList = mergeLists(l1, l2)
        
        return myList