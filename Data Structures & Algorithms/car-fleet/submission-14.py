class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []

        for p,s in pair:
            dest = (target - p) / s
            while stack and stack[-1] >= dest: # only adding faster values
                stack.pop()
            stack.append(dest)
        return len(stack)
        