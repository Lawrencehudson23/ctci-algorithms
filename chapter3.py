class StackNode:
    def __init__(self):
        self.items = []


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


# Sort Stack: Write a program to sort a stack such that the smallest items are on the top. You can use
# an additional temporary stack, but you may not copy the elements into any other data structure
# (such as an array). The stack supports the following operations: push, pop, peek, and is Empty.

# for element in stack[::-1]:
    # print element
    # [3.1: ThreeInOne ] Completed

# def threeInOne(arr):
#     stack1 = Stack()
#     stack2 = Stack()
#     stack3 = Stack()
#     arrLength = math.ceil( len(arr)/3 )

#     for i in range(len(arr)-1, -1, -1):
#         if len(arr) > 0:
#             if stack3.size() < arrLength:
#                 stack3.push( arr.pop() ) # is it better avoid mutating original array?
#             elif stack2.size() < arrLength:
#                 stack2.push( arr.pop() )
#             else:
#                 stack1.push( arr.pop() )

#     return [stack1.items, stack2.items, stack3.items]

# arr1 = [1, 2, 3, 6, 7, 8, 4, 5, 9, 10, 11, 13, 17, -1, 55]
# print(threeInOne(arr1))

    def sort(self):
        temp = Stack()
        final = Stack()
        max = self.peek()
        unSortedCount = self.size()
        while unSortedCount > 0:
            while self.size() > 0:
                if self.peek() > max:
                    max = self.peek()
                temp.push(self.pop())
            while temp.size() > 0:
                if temp.peek() == max:
                    unSortedCount -= 1
                    final.push(temp.pop())
                    # print(final.items)
                else:
                    self.push(temp.pop())
            if not self.isEmpty():
                max = self.peek()
        return final.items


newStack = Stack()
newStack.push(8)
newStack.push(5)
newStack.push(7)
newStack.push(1)

# print(newStack.size())
# print(newStack.size())
# newStack.sort()
# print("is empty", newStack.isEmpty())
# print("self size", newStack.size())
print(newStack.sort())
