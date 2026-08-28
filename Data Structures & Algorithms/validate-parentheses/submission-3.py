class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {"}" : "{", ")" : "(", "]" : "["}

        for c in s:
            if c in closeToOpen: # if we see a closed paranthese
                if stack and stack[-1] == closeToOpen[c]: # if we closed paranthese is equal to LI from s
                    stack.pop()
                else:
                    return False # means paranthese got closed by wrong { != )
            else:
                stack.append(c) # adding open paranthese
        
        if stack:
            return False
        else:
            return True