class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=False)
        stack = []
        for p,s in pair:
            dest = (target - p) / s
            while stack and stack[-1] <= dest: # delete faster cars
                stack.pop()
          
            stack.append(dest)
        return len(stack)
        