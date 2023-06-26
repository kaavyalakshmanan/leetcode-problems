class TimeMap:

    def __init__(self):

        self.store = {} # key = key, val = [[val, timestamp]]
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []

        self.store[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:

        res = ""
        values = self.store.get(key, [])

        if not values:
            return res

        # Run binary search on self.store[key]
        # O(logn)
        left, right = 0, len(values)-1
        while left <= right:
            mid = (right+left)//2
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                left = mid+1
            if values[mid][1] > timestamp:
                right = mid - 1

        return res

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
