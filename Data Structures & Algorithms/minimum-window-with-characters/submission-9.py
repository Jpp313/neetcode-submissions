class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        l = 0

        have = len(t)
        need = 0 
        min_length = 0

        countT = {}
        countS = {}

        res = [-1,-1]
        resLen = float("infinity")

        for i in range(len(t)):
            countT[t[i]] = 1 + countT.get(t[i], 0)


        for r in range(len(s)):
            countS[s[r]] = 1 + countS.get(s[r],0)

            if s[r] in countT and countT[s[r]] == countS[s[r]] : # looking to build valid substring
                need += 1

            while need == have: # have a valid substring
                length = (r - l + 1)
                if length < resLen:
                    min_length = length
                    res = [l,r]

                countS[s[l]] -= 1
                if s[l] in countT and countS[s[l]] - 1 < countT[s[l]]:
                    need -= 1
                l += 1

        
        return s[int(res[0]) : int(res[1]) + 1]