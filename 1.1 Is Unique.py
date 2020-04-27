# 1.1 Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures?
# Hints: #44, #117, #132


def isUnique(str):
    dic = {}
    for i in str:
        if i in dic:
            return False
        if i not in dic:
            dic[i] = 1
    return True


print(isUnique("abcd"))
