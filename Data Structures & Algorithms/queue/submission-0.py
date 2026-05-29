class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def append(self, value: int) -> None:
        new_node = Node(value)
        new_node.prev = self.tail.prev
        new_node.prev.next = new_node
        new_node.next = self.tail
        self.tail.prev = new_node


    def appendleft(self, value: int) -> None:
        new_node = Node(value)
        new_node.next = self.head.next
        new_node.next.prev = new_node
        new_node.prev = self.head
        self.head.next = new_node

    def pop(self) -> int:
        if self.isEmpty():
            return -1

        tmp = self.tail.prev
        self.tail.prev = tmp.prev
        tmp.prev.next = self.tail

        return tmp.val

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
            
        tmp = self.head.next
        self.head.next = tmp.next
        tmp.next.prev = self.head

        return tmp.val
        
