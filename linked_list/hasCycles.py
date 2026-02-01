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

def hasCycles(head: Optional[ListNode])->bool:
    fast = slow = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

        if fast is slow:
            return True
    return False
