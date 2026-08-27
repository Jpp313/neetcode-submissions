class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        freq_s = {}
        freq_t = {}

        for char in t:
            freq_t[char] = 1 + freq_t.get(char, 0)
        have = 0
        need = len(t)

        res = [-1,-1]
        resLen = float("infinity")

        l = 0
        for r in range(len(s)):
            freq_s[s[r]] = 1 + freq_s.get(s[r],0)

            if s[r] in freq_t and freq_t[s[r]] == freq_s[s[r]]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                freq_s[s[l]] -= 1
                if s[l] in freq_t and freq_s[s[l]] < freq_t[s[l]]:
                    have -= 1
                l += 1
        l,r = res
        if resLen != float("infinity"):
            return s[l: r + 1]
        else:
            return "" 
        
        