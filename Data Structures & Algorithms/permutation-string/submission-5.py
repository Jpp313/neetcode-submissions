class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        i = 0
        j = 0
        res = ""
        for j in range(len(s2)):

            if s2[j] not in s1:
                continue
            i = j
            res += s2[j]

            if sorted(res) == sorted(s1):
                return True
        return False

