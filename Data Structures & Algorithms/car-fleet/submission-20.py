class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        p = 0
        s = 0
        store = []
        for p,s in zip(position,speed):
            store.append((p,s))
        
        store.sort()
        
        stack = []
        for position, speed in store:
            time = (target - position) // speed

            while stack and stack[-1] <= time: # cars behind will catchup
                stack.pop() 
            stack.append(time)
        return len(stack) 
