class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class SLL:
    def __init__(self):
        self.head = None

    def printAll(self):
        current = self.head
        while current != None:
            print(current.val)
            current = current.next

    def addNode(self, val):
        if self.head == None:
            self.head = Node(val)
        else:
            newNode = Node(val)
            current = self.head
            while current.next != None:
                current = current.next
            current.next = newNode

    def addFront(self, val):
        newNode = Node(val)
        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def partitionAroundX(self, x):
        # Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition= 4]
        # 3, 5
        # 3, 5, 8,
        # 3, 5, 8, 5
        # 2, 3, 5, 8, 5
        # 1, 2, 3, 5, 8, 5

        # Output: [ 3 -> 1 -> 2 ] -> [ 10 -> 5 -> 5 -> 8 ]
        # left has #s less than 5 in any order
        # right has numbers 5 or greater in any order

        if self.head == None:
            return None
        if self.head.next == None:
            return "Cannot partition one node"

        current = self.head
        new = SLL()
        while current != None:
            if current.val < x:
                # print("CV: ", current.val)
                new.addFront(current.val)
            if current.val >= x:
                new.addNode(current.val)
            current = current.next
        return new


list1 = SLL()
list1.addNode(7)
list1.addNode(4)
list1.addNode(1)
list1.addNode(5)
list1.addNode(8)
list1.addNode(2)
list1.printAll()
print("----------------")
new1 = list1.partitionAroundX(6)
new1.printAll()
print("----------------")
#  2, 1, 4, 7, 5, 8
