class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(t) > len(s):
            return ""
        
        res = [-1, -1]
        resLen = float("infinity")

        window = {}
        countT = {}

        for char in t:
            countT[char] = 1 + countT.get(char, 0)
        
        l = 0
        have = 0
        need = len(countT)
        for r in range(len(s)):
            c = s[r]

            window[c] = 1 + window.get(c, 0)

            if s[r] in countT: # build have as we find the same chars in each
                have += 1

            while s[l] in window and have == need: # when we find valid substring
                length = r - l + 1
                if length < resLen:
                    res = l , r
                    resLen = length

                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] + 1 == countT[s[l]]:
                    have -= 1
                
                l += 1
                    
        l , r  = res
        if resLen != float("infinity"):
            return s[l : r + 1]
        else:
            return ""
