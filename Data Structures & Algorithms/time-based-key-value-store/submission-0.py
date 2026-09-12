class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store.pop(key,None)
        self.store[key].append((value,timestamp))


    def get(self, key: str, timestamp: int) -> str:
        return str(self.store[key][0][0])
