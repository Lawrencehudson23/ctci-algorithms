# 1.5 One Away: There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to check if they are
# one edit(or zero edits) away.
# EXAMPLE
# pale, ple - > true
# pales, pale - > true
# pale, bale - > true
# pale, bake - > false
# Hints:  # 23, #97, it 130


def oneAway(str1, str2):
    l1 = len(str1)
    l2 = len(str2)
    if l1-l2 > 1 or l2-l1 > 1:
        return False
    elif l1-l2 == 1:
        i = 0
        j = 0

        while i < l1:
            if str1[i] == str2[j]:
                i += 1
                j += 1
            elif str1[i] != str2[j]:
                i += 1
                if str1[i] != str2[j]:
                    return False
                else:
                    i += 1
                    j += 1
        return True
    elif l2-l1 == 1:
        i = 0
        j = 0

        while j < l2:
            if str1[i] == str2[j]:
                i += 1
                j += 1
            elif str1[i] != str2[j]:
                j += 1
                if str1[i] != str2[j]:
                    return False
                else:
                    i += 1
                    j += 1
        return True
    else:
        count = 0
        for i in range(l1):
            if str1[i] != str2[i]:
                count += 1
            if count > 1:
                return False
        return True


print(oneAway("pace", "pale"))
