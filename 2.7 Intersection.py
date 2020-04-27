# Intersection; Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting node. Note that the intersection is defined based on reference, not value. That is, if the kth
# node of the first linked list is the exact same node (by reference) as the jth node of the second
# linked list, then they are intersecting.
# Hints: #20, #45, #55, #65, #76, #93, #1 1 1, #120, #129

#                                         c1
# l1 => a[1] -> b[3 ] -> c[7]    x  - a  -b - c - d - f - g - h
#                                     |
# l2 => e[4] -> a[1] -> b[3]      e - b - c - d - f - g
#


class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None


class SLList:

    def __init__(self):
        self.head = None

    def addToFront(self, val):
        newNode = SLNode(val)
        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        return self

    def printValues(self):
        runner = self.head
        while(runner != None):
            print(runner.value)
            runner = runner.next
        return self

    def addToEnd(self, val):
        newNode = SLNode(val)
        if self.head == None:
            newNode = self.head
            return self

        runner = self.head
        while(runner.next != None):
            runner = runner.next
        runner.next = newNode
        return self

    def addNodeToFront(self, n):
        if self.head == None:
            self.head = n
            return self
        else:
            n.next = self.head
            self.head = n
        return self


def intersectedNode(SLL1, SLL2):
    c1 = SLL1.head
    c2 = SLL2.head
    while c1.next != None:
        if c1 == c2:
            return c1

        c2 = c2.next

        if c2 == None:
            c2 = SLL2.head
            c1 = c1.next


l1 = SLList()
node1 = SLNode(1)
node2 = SLNode(2)
node3 = SLNode(3)
node4 = SLNode(4)
node5 = SLNode(5)
node6 = SLNode(6)


node7 = SLNode(7)
node8 = SLNode(8)

l1.addNodeToFront(node1)
l1.addNodeToFront(node2)
l1.addNodeToFront(node3)
l1.addNodeToFront(node4)
l1.addNodeToFront(node5)
l1.addNodeToFront(node6)
6-5-4-3-2-1

print("printing values of l1")
l1.printValues()

l2 = SLList()

# l2.addNodeToFront(node1)
# l2.addNodeToFront(node2)
l2.addNodeToFront(node1)
l2.addNodeToFront(node4)
l2.addNodeToFront(node7)
l2.addNodeToFront(node8)


# 8-7-4-1
# 6-5-4-1
# l2.addNodeToFront(node5)

print("return: " + str(intersectedNode(l1, l2)))
print(node4)
print(node5)
print("printing values of l2")
l2.printValues()
print("printing values of l1")
l1.printValues()
