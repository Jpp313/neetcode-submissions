class Solution:
    def isValid(self, s: str) -> bool:
        open_p = [] 
        closeToOpen = {"}" : "{", "]" : "[", ")" : "("}
      
        for c in s:
            
            if c in closeToOpen: # close paranthese condition
                if open_p and open_p[-1] == closeToOpen[c]:
                    open_p.pop()
                else:
                    return False
            else:
                open_p.append(c)
        
        return len(open_p) == 0