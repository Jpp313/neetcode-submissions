class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)

        stack = []

        for position, speed in pair:
            
            dest = (target - position) // (speed)

            while stack and stack[-1] >= dest:
                stack.pop()
            stack.append(dest)

        return len(stack)