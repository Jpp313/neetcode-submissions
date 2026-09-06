class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        closeToOpen = {"]" : "[", "}" : "{", ")" : "("}

        for sym in s:
            if sym in closeToOpen: # if close paranthese
                if stack[-1] != closeToOpen[sym]: # close paranthese wasnt preceded by an open parantehse of same type
                    return False
                else:
                    stack.pop()
            else:
                stack.append(sym)

        return len(stack) == 0