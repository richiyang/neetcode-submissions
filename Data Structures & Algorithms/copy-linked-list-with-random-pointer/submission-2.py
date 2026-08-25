"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
        nton = {head: Node(head.val)}
        node = head

        while node:
            tempNode = nton[node]
            if node.next and node.next not in nton:
                nton[node.next] = Node(node.next.val)
            if node.random and node.random not in nton:
                nton[node.random] = Node(node.random.val)
            
            tempNode.next = nton[node.next] if node.next else None
            tempNode.random = nton[node.random] if node.random else None
            node = node.next
        
        return nton[head]
