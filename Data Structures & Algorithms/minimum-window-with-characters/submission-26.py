class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        countT = {}
        window = {}

        resLen = float("infinity")
        res = [-1,-1]
        l = 0
        

        for i in range(len(t)):
            countT[t[i]] = 1 + countT.get(t[i], 0)

        have = 0
        need = len(countT)

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]: # counting until everything in t is in s
                have += 1
            
            while have == need: # when we finally have a substring
                length = r - l + 1
                if length < resLen:
                    resLen = length
                    res = l , r
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] + 1 == countT[s[l]]: # if we just removed a match
                    have -= 1
                l += 1 # look for more shorter substrings if we still have all of s in t
        if resLen != float("infinity"):
            l , r = res
            return s[l : r + 1]
        else:
            return ""