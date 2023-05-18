class Vector2D:

    def __init__(self, vec: List[List[int]]):

        # O(n*m) time O(n*m) space

        self.arr = []
        if vec:
            rows = len(vec)
            for row in range(rows):
                for col in range(len(vec[row])):
                    self.arr.append(vec[row][col])

        self.idx = 0
        

    def next(self) -> int:

        # OP(1) time O(1) space

        currVal = self.arr[self.idx]
        self.idx+=1
        return currVal




    def hasNext(self) -> bool:

         # OP(1) time O(1) space

        if self.idx < len(self.arr):
            return True
        return False
        


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()
