from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

def createList(items:list[int]):

    head = ListNode(items[0])
    curr = head
    for i in range(1,len(items)):
        curr.next = ListNode(items[i])
        curr = curr.next
    return head

def removeNthFromEnd(head: Optional[ListNode], n: int)-> Optional[ListNode]:

    dummy = ListNode()
    dummy.next = head
    ahead = dummy
    behind = dummy
    i=0
    while i < n+1:
        ahead = ahead.next
        i+=1
    
    while ahead:
        behind= behind.next
        ahead = ahead.next

    behind.next = behind.next.next

    return dummy.next




list1 = createList([1,2])
n=1
printList(removeNthFromEnd(list1,n))



