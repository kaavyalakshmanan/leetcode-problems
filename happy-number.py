class Solution:
    def isHappy(self, n: int) -> bool:

        # # O(logn) time because we are processing each digit in the curr number and the number of digits in a number is given by logn
        # # O(logn) space because we will be putting logn values in the hash set

        # i = n
        # squares = set()

        # while i not in squares:
        #     if i == 1:
        #         return True
        #     j = i
        #     curr = 0
        #     while j > 0:
        #         curr += ((j % 10) ** 2)
        #         j = j // 10
        #     squares.add(i)
        #     i = curr

        # return False

    # we can optimize this algo by not using extra space using floyds cycle finding algo
    # O(logn) time O(1) space

        slow = n
        fast = self.getNext(n)

        while fast != 1 and fast != slow:
            slow = self.getNext(slow)
            fast = self.getNext(self.getNext(fast))

        return fast == 1

    def getNext(self, n: int) -> int:

        totalSum = 0
        while n > 0:
            totalSum += ((n % 10) ** 2)
            n = n//10

        return totalSum



    



        
