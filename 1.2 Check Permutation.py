# 1.2 Check Permutation: Given two strings, write a method to decide if one is a permutation of the
# other.
# Hints: ft,  # 84, #122, #131


def isPermutate(str1, str2):
    if len(str1) != len(str2):
        return False

# use sorted()
#     if sorted(str1) != sorted(str2):
#         return False
#     return True
    dic1 = {}
    dic2 = {}
    for i in str1:
        if i not in dic1:
            dic1[i] = 1
        else:
            dic1[i] += 1
    for j in str2:
        if j not in dic2:
            dic2[j] = 1
        else:
            dic2[j] += 1
    if dic1 != dic2:
        return False
    return True


print(isPermutate("cTba", "abcT"))
