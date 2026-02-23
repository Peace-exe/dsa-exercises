from typing import Optional
from math import ceil
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

def middleNode(head: Optional[ListNode])-> Optional[ListNode]:

    length = 0
    curr = head

    while curr:
        length+=1
        curr = curr.next

    mid = ceil(length//2)
    pos = 0
    curr= head
    
    while curr:

        if pos == mid:
            return curr
        else:
            pos+=1
            curr=curr.next

    

list1 = createList([1,2,3,4,5,6])
printList(middleNode(list1))
