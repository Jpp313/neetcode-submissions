class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        
        l = 0
        r = len(self.store[key]) - 1
        t = 0
        while l <= r:
            mid = l + (r - l) // 2
            if int(self.store[key][mid][0]) <= timestamp:
                t = mid
                l = mid + 1
            elif int(self.store[key][mid][0]) > timestamp:
                r = mid - 1
            
        return str(self.store[key][t][1])

