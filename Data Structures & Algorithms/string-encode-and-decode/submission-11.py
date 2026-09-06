class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s
        return res

        # length is for how long we want to move our pointer to slice and cover full word # allows us to track length if was 2 digits and the last char always before start of new word

    def decode(self, s: str) -> List[str]:
        i = 0
        j = 1
        strs = []
        while j < len(s):
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j += length + 1
            word = s[i:j]
            strs.append(word)
            i = j
        return strs


