from typing import Optional
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
def createList(arr):
    """
    arr: List[List[int | None]]
    Example:
    [[7,None],[13,0],[11,4],[10,2],[1,0]]

    returns: head of linked list
    """

    if not arr:
        return None

    # ---------- PASS 1: Create all nodes ----------
    nodes = [Node(val) for val, _ in arr]

    # connect next pointers
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i+1]

    # ---------- PASS 2: Assign random pointers ----------
    for i, (_, random_index) in enumerate(arr):
        if random_index is not None:
            nodes[i].random = nodes[random_index]

    return nodes[0]


def copyRandomList(head: 'Optional[Node]') -> 'Optional[Node]':
        
        if head is None:
            return None

        hashmap = {}

        curr = head
        while curr:
             hashmap[curr]= Node(curr.val)
             curr=curr.next
        
        for key in hashmap:
            if key.next is not None:
                hashmap[key].next = hashmap[key.next]
            else:
                hashmap[key].next = None
            
            if key.random is not None:
                hashmap[key].random = hashmap[key.random]
            else:
                hashmap[key].random=None
        
        return hashmap[head]


            
        



head = createList([[7,None],[13,0],[11,4],[10,2],[1,0]])
print(copyRandomList(head))