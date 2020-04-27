# 1.4 Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation
# is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
# EXAMPLE
# Input: Tact Coa
# Output: True (permutations: "taco cat", "atco eta", etc.)
# Hints:  # 106, h 0134,  136


def isPalindromePermutation(oldStr):
    str = oldStr.lower()
    dic = {}
    for i in str:
        if i not in dic and i != " ":
            dic[i] = False
        elif i in dic:
            dic[i] = not dic[i]
    count = 0
    for k, v in dic.items():
        if v == False:
            count += 1
    if count > 1:
        return False
    return True


print(isPalindromePermutation("Tact Coa"))
