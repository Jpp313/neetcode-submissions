class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        need = {}
        window = {}

        for c in s1:
            need[c] = need.get(c, 0) + 1

        l = 0
        for r in range(len(s2)):
            c = s2[r]
            window[c] = window.get(c, 0) + 1

            if r - l + 1 > len(s1):
                window[s2[l]] -= 1
                l += 1

            if window == need:
                return True

        return False