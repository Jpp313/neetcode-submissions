class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        need = {}
        window = {}

        for c in s1:
            need[c] = need.get(c, 0) + 1

        for r, c in enumerate(s2):
            window[c] = window.get(c, 0) + 1

            if r >= len(s1):
                left = s2[r - len(s1)]
                window[left] -= 1
                if window[left] == 0:
                    del window[left]

            if window == need:
                return True

        return False