class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": # empty base case
            return ""

        countT = {}
        window = {} # made to track disnct cahracters as we build window ands when we need to know if we are at a substring

        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        l = 0
        need = len(countT)
        have = 0

        res = [-1,-1]
        resLen = float("infinity")

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]: # char in t and if the freq is the same
                have += 1
            while have == need: # when we have a valid substring
                if (r - l + 1) < resLen: # record min length if applicable
                    res = [l, r]
                    resLen = r - l + 1
                
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] + 1 == countT[s[l]]: # if we lose the char when sliding right must adjust have
                    have -= 1
                l += 1
        
        l, r = res

        if resLen != float("infinity"):
            return s[l : r + 1]
        else:
            return ""
                
                