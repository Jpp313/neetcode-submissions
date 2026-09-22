class Solution:
    def isValid(self, s: str) -> bool:
        
        closeToOpen = { "}" : "{", ")" : "(", "]" : "["}

        stack = [] # holds all open brackets

        for sym in s:
            if stack and sym in closeToOpen: # it is a close symbol
                open_sym = stack.pop()
                if open_sym != closeToOpen[sym]:
                    return False
            else: # add open sym to stack
                stack.append(sym)

        return len(stack) == 0
            
