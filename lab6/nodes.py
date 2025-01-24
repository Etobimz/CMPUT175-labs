class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Slinked:
    def __init__(self):
        self.head = None
    def printl(self):
        current = self.head
        while current:
            print(current.data, end='')
            current = current.next
        

l = Slinked()
l.head = Node('head\t')
l.head.next = Node('ll\t')
l.head.next.next = Node('pp')
l.printl()
