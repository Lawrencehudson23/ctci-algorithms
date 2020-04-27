# 1.6 String Compression: Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3, If the
# "compressed" string would not become smaller than the original string, your method should return
# the original string. You can assume the string has only uppercase and lowercase letters(a - z).
# Hints:  # 92, if 110


def stringCompress(string):
    newstring = string[0]
    count = 1
    for i in range(1, len(string)):
        # if count==0:
        #     newstring+=string[i]
        #     count+=1
        if string[i] == string[i-1]:
            count += 1
        else:
            newstring += str(count)
            newstring += string[i]
            count = 1
    newstring += str(count)

    if len(newstring) > len(string):
        return string

    return newstring


print(stringCompress("aabcccccaaaa"))
