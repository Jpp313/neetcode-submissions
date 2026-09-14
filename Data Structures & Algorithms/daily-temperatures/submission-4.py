class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        output = [0] * len(temperatures)

        for i in range(len(temperatures)):
            t = temperatures[i]

            while stack and stack[-1][0] < t: # we see a warmer temp
                stackT,stackInd = stack.pop()
                output[stackInd] = i - stackInd

            stack.append((t,i))
        return output