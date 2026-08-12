class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}


        count1 = [0] * 26
        count2 = [0] * 26

        for i in range(len(s)):
            count1[ord(s[i]) - ord('a')] += 1
        
        for i in range(len(t)):
            count2[ord(t[i]) - ord('a')] += 1

        return count1 == count2