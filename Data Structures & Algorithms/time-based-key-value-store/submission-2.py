class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        pairs = self.store[key]  # list of (value, timestamp) tuples
        lo = 0
        hi = len(pairs) - 1
        if timestamp < pairs[0][1]:
            return ""

        while lo < hi:
            mid = (lo + hi + 1) // 2
            if pairs[mid][1] == timestamp:
                return pairs[mid][0]
            elif pairs[mid][1] < timestamp:
                lo = mid
            else:
                hi = mid - 1
        if lo == hi:
            return pairs[lo][0]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)