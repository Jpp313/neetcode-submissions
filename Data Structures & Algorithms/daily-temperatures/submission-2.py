class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # temp, index

        for i in range(len(temperatures)):
            temp = temperatures[i]
            while stack and stack[-1][0] < temp:
                stackT, stackInd = stack.pop()
                print(stackInd)
                res[stackInd] = i - stackInd
            stack.append((temp, i))
        return res