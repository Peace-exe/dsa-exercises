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

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode])-> Optional[ListNode]:
    res = ListNode()
    curr = res

    while list1 and list2:

        if list1.val < list2.val:
            curr.next = list1
            curr = list1
            list1 = list1.next
            
        else:
            curr.next = list2
            curr = list2
            list2 = list2.next
    
    curr.next = list1 if list1 else list2

    return res.next

list1 = createList([1,2,4])
list2 = createList([1,3,4])
printList(mergeTwoLists(list1,list2))


