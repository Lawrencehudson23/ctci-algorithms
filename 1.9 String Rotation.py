# 1.9 String Rotation; Assume you have a method isSubstring which checks if one word is a substring
# of another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one
# call to isSubstring [e.g., "water bottle " is a rotation oP'erbottlewat"),
# Hints: #34, #88,#W4
# p'j 206
# Additional Questions: Object-Oriented Design (#7.12), Recursion (#8.3), Sorting and Searching (#10.9), C++
# (#12.11), Moderate Problems (#16.8, #16.17, #16,22), Hard Problems (#17.4, #17.7, #17.13, #17.22, #17,26).
# Hints start on page 653.


def isSubstring(str1, str2):
    if len(str1) < len(str2):
        subString = str1
        string = str2
    if len(str1) >= len(str2):
        subString = str2
        string = str1

    i = 0
    j = 0
    matchCount = len(subString)
    while i < len(string):

        if string[i] == subString[j]:
            i += 1
            j += 1
            matchCount -= 1
            if matchCount == 0:
                return True

        elif string[i] != subString[j]:
            i += 1
            j = 0
            matchCount = len(subString)

    return False


def isStringRotation(s1, s2):
    if len(s1) != len(s2):
        return False
    s3 = s1+s1

    if isSubstring(s3, s2) == True:
        return True
    return False


# print(isSubstring("botet", "waterbottle"))
print(isStringRotation("erbottlywat", "waterbottle"))
