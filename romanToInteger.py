class Solution:
    def romanToInt(self, s: str) -> int:
        dictionary = {
            "I":1,
            
            "V":5,
            "X":10,
            
            "L":50,
            "C":100,

            "D":500,
            "M":1000,
        }
        
        sum = 0

        myIter = iter(range(0, len(s)))
        for i in myIter:
            if i+1 < len(s):
                if dictionary[s[i]] < dictionary[s[i+1]]:
                    sum += (dictionary[s[i+1]]-dictionary[s[i]])
                    print("i: ", i)
                    print("s[i]<s[i+1]: ", sum)
                    next(myIter, None)
                elif dictionary[s[i]] >= dictionary[s[i+1]]:
                    print("i: ", i)
                    sum += dictionary[s[i]]
                    print("s[i]>=s[i-1]: ", sum)
            elif i+1 == len(s):
                print("i: ", i)
                sum += dictionary[s[i]]
                    
        
        # print(type(sum))
        return sum


            #     M CM XC IV
            #     1  9  9  4
            #  1000 900 90 4

# VII = 7
# VIII = 8
# IX = 9

    
solution = Solution()
# print(solution.romanToInt("LVIII"))
print(solution.romanToInt("MCMIV"))

# XXVII = 27