from typing import Optional

class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

def deleteDuplicates(head : Optional[ListNode])-> Optional[ListNode]:

    current = head
 
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    
    return head

head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)
deleteDuplicates(head)
printList(head)
