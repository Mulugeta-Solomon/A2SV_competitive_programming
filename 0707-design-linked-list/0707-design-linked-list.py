class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None  
        
    def get(self, index: int) -> int:
        
        curr, idx = self.head, 0
        while curr:   
            if idx == index:
                return curr.value 
            curr = curr.next
            idx += 1

        return -1

    def addAtHead(self, val: int) -> None:
       self.head = Node(val, self.head)
 
    def addAtTail(self, val: int) -> None:

        node = Node(val)
        if not self.head:
            self.head = node
            return 
        
        curr = self.head
        while curr.next:
            curr = curr.next
        
        curr.next = node

    def addAtIndex(self, index: int, val: int) -> None:
        dummy = Node(0, self.head)
        node = Node(val)
        prev, curr, idx = dummy, self.head, 0 

        while curr:
            if idx == index:
                prev.next = node
                node.next = curr
                break
            curr = curr.next
            prev = prev.next
            idx += 1
        
        if idx == index:
            prev.next = node 
        
        self.head = dummy.next

    def deleteAtIndex(self, index: int) -> None:
        dummy = Node(0, self.head)

        prev, curr, idx = dummy, self.head, 0
        while curr:
            if idx == index:
                prev.next = curr.next
                break
            curr = curr.next
            prev = prev.next
            idx += 1
        
        self.head = dummy.next
        
      
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)