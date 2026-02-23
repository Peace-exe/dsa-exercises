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
        hashmap = {}

        curr = head
        i=0
        while curr:
            hashmap[int(i)]= Node(curr.val)
            i+=1
        return hashmap

print(create())