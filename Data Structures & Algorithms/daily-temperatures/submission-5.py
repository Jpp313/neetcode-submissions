class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []

        output = [0] * len(temperatures)

        for t in range(len(temperatures)):

            while stack and stack[-1][0] < temperatures[t]:
                stackT,stackInd = stack.pop()
                days = t - stackInd
                output[stackInd] = days
            
            stack.append((temperatures[t],t))

        return output