# 1.1 Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures?
# Hints: #44, #117, #132


# def isUnique(str):
#     dic = {}
#     for i in str:
#         if i in dic:
#             return False
#         if i not in dic:
#             dic[i] = 1
#     return True


# print(isUnique("abcd"))

# 1.2 Check Permutation: Given two strings, write a method to decide if one is a permutation of the
# other.
# Hints: ft,  # 84, #122, #131


# def isPermutate(str1, str2):
#     if len(str1) != len(str2):
#         return False

# # use sorted()
# #     if sorted(str1) != sorted(str2):
# #         return False
# #     return True
#     dic1 = {}
#     dic2 = {}
#     for i in str1:
#         if i not in dic1:
#             dic1[i] = 1
#         else:
#             dic1[i] += 1
#     for j in str2:
#         if j not in dic2:
#             dic2[j] = 1
#         else:
#             dic2[j] += 1
#     if dic1 != dic2:
#         return False
#     return True


# print(isPermutate("cTba", "abcT"))

# 1.3 URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
# has sufficient space at the end to hold the additional characters, and that you are given the "true"
# length of the string. (Note: If implementing in Java, please use a character array so that you can
#                        perform this operation in place.)
# EXAMPLE
# Input: "Mr 3ohn Smith 13
# Output: "Mr%203ohn%20Smith"
# Hints:  # 53,0118


# def URLify(str):
#     newStr = ""
#     for i in str:
#         if i != " ":
#             newStr += i
#         else:
#             newStr += '%20'
#     return newStr


# print(URLify("I have a dream"))

# 1.4 Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation
# is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
# EXAMPLE
# Input: Tact Coa
# Output: True (permutations: "taco cat", "atco eta", etc.)
# Hints:  # 106, h 0134,  136


# def isPalindromePermutation(oldStr):
#     str = oldStr.lower()
#     dic = {}
#     for i in str:
#         if i not in dic and i != " ":
#             dic[i] = False
#         elif i in dic:
#             dic[i] = not dic[i]
#     count = 0
#     for k, v in dic.items():
#         if v == False:
#             count += 1
#     if count > 1:
#         return False
#     return True


# print(isPalindromePermutation("Tact Coa"))

# 1.5 One Away: There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to check if they are
# one edit(or zero edits) away.
# EXAMPLE
# pale, ple - > true
# pales, pale - > true
# pale, bale - > true
# pale, bake - > false
# Hints:  # 23, #97, it 130


# def oneAway(str1, str2):
#     l1 = len(str1)
#     l2 = len(str2)
#     if l1-l2 > 1 or l2-l1 > 1:
#         return False
#     elif l1-l2 == 1:
#         i = 0
#         j = 0

#         while i < l1:
#             if str1[i] == str2[j]:
#                 i += 1
#                 j += 1
#             elif str1[i] != str2[j]:
#                 i += 1
#                 if str1[i] != str2[j]:
#                     return False
#                 else:
#                     i += 1
#                     j += 1
#         return True
#     elif l2-l1 == 1:
#         i = 0
#         j = 0

#         while j < l2:
#             if str1[i] == str2[j]:
#                 i += 1
#                 j += 1
#             elif str1[i] != str2[j]:
#                 j += 1
#                 if str1[i] != str2[j]:
#                     return False
#                 else:
#                     i += 1
#                     j += 1
#         return True
#     else:
#         count = 0
#         for i in range(l1):
#             if str1[i] != str2[i]:
#                 count += 1
#             if count > 1:
#                 return False
#         return True


# print(oneAway("pace", "pale"))

# 1.6 String Compression: Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3, If the
# "compressed" string would not become smaller than the original string, your method should return
# the original string. You can assume the string has only uppercase and lowercase letters(a - z).
# Hints:  # 92, if 110


# def stringCompress(string):
#     newstring = string[0]
#     count = 1
#     for i in range(1, len(string)):
#         # if count==0:
#         #     newstring+=string[i]
#         #     count+=1
#         if string[i] == string[i-1]:
#             count += 1
#         else:
#             newstring += str(count)
#             newstring += string[i]
#             count = 1
#     newstring += str(count)

#     if len(newstring) > len(string):
#         return string

#     return newstring


# print(stringCompress("aabcccccaaaa"))

# 1.7 Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
# bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
# Hints: 51, 0100
# array = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16]
# ]


# def rotateMatrix(mat):
#     for i in range(len(mat)-1):
#         for j in range(i, (len(mat)-1-i)):
#             mat[i][j], mat[i+j][len(mat)-1-i] = mat[i +
#                                                     j][len(mat)-1-i], mat[i][j]
#             mat[i+j][len(mat)-1-i], mat[len(mat)-1-i][len(mat) - 1 -
#                                                       j] = mat[len(mat)-1-i][len(mat) - 1-j], mat[i+j][len(mat)-1-i]
#             mat[len(mat)-1-i][len(mat)-1-j], mat[len(mat)-1 -
#                                                  j][i] = mat[len(mat)-1-j][i], mat[len(mat)-1-i][len(mat)-1-j]


# print(rotateMatrix(array))
# [13, 9, 5, 1]
# [14, 10, 6, 2]
# [15, 11, 7, 3]
# [16, 12, 8, 4]


# 1.1
# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures?

# def isUnique (string):
#     for i in range(len(string)):
#         currentChar = string[i]
#         for j in range(i+1, len(string)):
#             if string[j] == currentChar:
#                 return False
#     return True
# print(isUnique(str))

# 1.2
# Check Permutation: Given two strings, write a method to decide if one is a permutation of the
# other.

# def isPermutation(str1, str2):
#     charCounter = {}
#     for i in str1:
#         if i not in charCounter:
#             charCounter[i] = 1
#         else:
#             charCounter[i] += 1
#     for i in str2:
#         if i in charCounter:
#             charCounter[i] -= 1
#             if charCounter[i] == 0:
#                 charCounter.pop(i)
#         else:
#             charCounter[i] = 1
#     if charCounter == {}:
#         return True
#     return False

# str1="abcc"
# str2="cabcc"

# print(isPermutation(str1,str2))


# 1.7
# Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
# bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

# import math;
# def rotate(matrix):
#     if len(matrix) == 0 or len(matrix) != len(matrix[0]):
#         return False
#     n = len(matrix)
#     for layer in range(math.ceil(n/2)):
#         first = layer
#         last = n - 1 - layer
#         for i in range(first,last):
#             offset = i - first
#             top = matrix[first][i]

#             # left -> top
#             matrix[first][i ] = matrix[last-offset][first]

#             # bottom -> left
#             matrix[last-offset][first ] = matrix[last][last - offset]

#             # right ~> bottom
#             matrix[last][last - offset ] = matrix[i][last]

#             # top -> right
#             matrix[i][last ] = top
#             #right <- saved top
#     return matrix

# matrix = [
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12],
#     [13,14,15,16]
# ]

# # matrix = [
# #     [1,2,3],
# #     [4,5,6],
# #     [7,8,9]
# # ]

# print(rotate(matrix))


# 2.3 Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but
# the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
# that node.

# class Node:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next


# class SLL:
#     def __init__(self):
#         self.head = None

# def printAll(self):
#     current = self.head
#     while current != None:
#         print(current.val)
#         current = current.next

#     def addNode(self, val):
#         if self.head == None:
#             self.head = Node(val)
#         else:
#             newNode = Node(val)
#             current = self.head
#             while current.next != None:
#                 current = current.next
#             current.next = newNode

#     def removeFromMiddle(self, val):
#         if self.head == None or self.head.next == None:
#             return False
#         current = self.head
#         while current.next != None:
#             if current.next.val == val and current.next.next != None:
#                 current.next = current.next.next
#                 isRemoved = True
#                 return
#             current = current.next
#         print("the value does not exist")


# list = SLL()
# list.addNode("a")
# list.addNode("b")
# list.addNode("c")
# list.addNode("c")
# list.addNode("d")
# list.addNode("c")
# list.addNode("e")
# # list.printAll()
# list.removeFromMiddle("c")
# list.printAll()

# 2.5 Sum Lists: You have two numbers represented by a linked list, where each node contains a single
# digit. The digits are stored in reverse order, such that the Vs digit is at the head of the list. Write a
# function that adds the two numbers and returns the sum as a linked list.
# EXAMPLE
# Input: (7- > 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295.
# Output: 2 -> 1 -> 9. That is, 912.
# FOLLOW UP
# Suppose the digits are stored in forward order. Repeat the above problem.
# EXAMPLE
# Input: (6 -> 1 -> 7) + (2 -> 9 -> 5).That is, 617 + 295,
# Output:9 -> 1 -> 2,Thatis,912.
# Hints: #7, #30, #71 #95, #109
# class Node:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next

# class SLL:
#     def __init__ (self):
#         self.head = None

#     def printAll(self):
#         current = self.head
#         while current != None:
#             print(current.val)
#             current = current.next

#     def addNode(self, val):
#         if self.head == None:
#             self.head = Node(val)
#         else:
#             newNode = Node(val)
#             current = self.head
#             while current.next != None:
#                 current = current.next
#             current.next = newNode

#     def removeFromMiddle(self, val):
#         if self.head == None or self.head.next == None:
#             return False
#         current = self.head
#         while current.next != None:
#             if current.next.val == val and current.next.next != None:
#                 current.next = current.next.next
#                 isRemoved = True
#                 return
#             current = current.next
#         print("the value does not exist")

# def sumLists (SLL1, SLL2):
#     if SLL1.head == None and SLL2.head == None:
#         return None
#     elif SLL1.head == None:
#         return SLL2
#     elif SLL2.head == None:
#         return SLL1
#     else:
#         current = SLL1.head
#         power = 0
#         number1 = 0
#         while (current != None):
#             number1 += (current.val * (10**power))
#             power += 1
#             current = current.next

#         current = SLL2.head
#         power = 0
#         number2 = 0
#         while (current != None):
#             number2 += (current.val * (10**power))
#             power += 1
#             current = current.next
#         sum = number1 + number2
#         strSum = str(sum)
#         print(strSum)
#         newList = SLL()
#         for i in range(len(strSum)-1, -1, -1):
#             newList.addNode(strSum[i])
#         return newList.printAll()

# SLL1 = SLL()
# SLL1.addNode(7)
# SLL1.addNode(1)
# SLL1.addNode(6)

# SLL2 = SLL()
# SLL2.addNode(5)
# SLL2.addNode(9)
# SLL2.addNode(2)

# sumLists(SLL1,SLL2)


# 2.4 Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
# before all nodes greater than or equal to x. Ifxis contained within the list, the values of x only need
# to be after the elements less than x(see below). The partition element x can appear anywhere in the
# "right partition"
# it does not need to appear between the left and right partitions.
# EXAMPLE
# Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition = 5]
# Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
# Hints:  # 3, #24
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
new1 = list1.partitionAroundX(5)
new1.printAll()
print("----------------")
