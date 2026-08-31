class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(t) > len(s):
            return ""

        res = [-1,-1]
        resLen = float("infinity")

        window = {}
        countT = {}

        for i in range(len(t)): # build out freq chars for t length
            countT[t[i]] = 1 + countT.get(t[i], 0)
            window[s[i]] = 1 + window.get(s[i], 0)
        
        l = 0
        have = 0
        need = len(countT)
        
        for r in range(len(t),len(s)):
            c = s[r]
            window[c] = 1 + window.get(c,0) # building window list
            if c in countT:
                have += 1
            while have == need: # when we have valid substring
                if (r - l + 1) < resLen: # check to update resLen if we have a min length
                    res = [l , r]
                    resLen = (r - l + 1)
                window[s[l]] -= 1

                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        l , r = res
        if resLen != float("infinity"):
            return s[l : r + 1]
        else:
            return ""
        
        
