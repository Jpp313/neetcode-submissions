class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            stack.append(s[i])
            if s[i] == "}":
                if "{" not in stack:
                    return False
            if s[i] == "]":
                if "[" not in stack:
                    return False
            if s[i] == ")":
                if "(" not in stack:
                    return False
        return True
