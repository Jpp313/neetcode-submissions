class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        stack = set()
        i = 0
        for i in range(len(position)):
            count = 0
            while target > position[i]:
                position[i] += speed[i]
                count += 1
            else:
                stack.add(count)
        return len(stack)
        
        