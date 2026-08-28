class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid = ["[", "{", "("]
        for i in range(len(s)):
            if s[i] in valid:
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
