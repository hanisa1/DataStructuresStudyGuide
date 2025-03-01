class CNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = CNode(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head  # Circular link
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = new_node
        new_node.next = self.head  # Circular link

    def display(self, count=10):  # Avoid infinite loop in case of circular list
        if not self.head:
            return
        temp = self.head
        for _ in range(count):
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(Back to Head)")

# Example Usage
cll = CircularLinkedList()
cll.append(100)
cll.append(200)
cll.append(300)
cll.display()