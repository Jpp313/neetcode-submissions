class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        i = 0
        for j in range(len(s2)):

            if s2[j] not in s1:
                continue
            else:
                res = ""
                while s2[j] in s1:
                    res += s2[j]
                    j += 1
                
                if sorted(res) == sorted(s1):
                    return True
                

        return False

