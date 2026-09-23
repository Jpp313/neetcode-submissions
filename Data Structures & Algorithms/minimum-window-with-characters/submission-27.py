class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(t) > len(s):
            return ""

        l = 0

        countT = {}
        for letter in t:
            countT[letter] = 1 + countT.get(letter,0)

        window = {}
        have = 0
        need = len(countT)
        min_length = 0

        res = [-1,-1]
        resLen = float("infinity")
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c,0) # add freq to dict

            if c in countT and window[c] == countT[c]: # letter and freq are the same
                have += 1
            while have == need: # we found a substring
                length = (r - l) + 1
                if length < resLen:
                    resLen = length
                    res = l, r
                window[s[l]] -= 1
                if s[l] in countT and countT[s[l]] - 1 == window[s[l]]: # if letter was part of substring
                    have -= 1
                l += 1
        
        l , r = res
        if resLen == float("infinity"):
            return ""
        else:
            return s[l:r+1]

