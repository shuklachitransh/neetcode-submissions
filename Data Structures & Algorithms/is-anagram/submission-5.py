from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        check = Counter(s)

        for ch in t:
            if ch in check:
                if check[ch] > 0:
                    check[ch] -= 1
                else:
                    return False
            else:
                return False
        return True 
        


            
