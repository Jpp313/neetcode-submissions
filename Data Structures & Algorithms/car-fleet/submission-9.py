class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        store = [(p, s) for p, s in zip(position, speed)]

        store.sort(reverse=False)
        stack = []

        for p, s in store:
            time = (target - p) / s

            while stack and stack[-1] <= time:
                stack.pop()
            stack.append(time)
        print(stack)
        return len(stack)