class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] 
        output = [0] * len(temperatures)
        # add to stack when temp is greater than prev
        for i in range(len(temperatures)):
            t = temperatures[i]
            while stack and stack[-1][0] < t: # finding a warmer temp
                stackT, stackInd = stack.pop() # record old cool temp and day it was cool
                output[stackInd] = i - stackInd # find diff of days to see cool - warm and days in bet
            stack.append((t, i)) # adding cooler temps to stack

        return output