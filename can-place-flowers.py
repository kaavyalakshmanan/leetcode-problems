class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        # O(n) time O(1) space
        
        numFlowers = n
        for i in range(len(flowerbed)):
            if numFlowers == 0:
                    return True
            if flowerbed[i] == 1:
                continue
            left = flowerbed[i-1] if i-1 >= 0 else -1
            right = flowerbed[i+1] if i+1 < len(floclass Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        # O(n) time O(1) space

        numFlowers = n
        i = 0
        while i < len(flowerbed):
            if numFlowers == 0:
                return True
            f = flowerbed[i]
            left = flowerbed[i-1] if i-1 >= 0 else 0
            right = flowerbed[i+1] if i+1 < len(flowerbed) else 0
            if f == 0 and left == 0 and right == 0:
                numFlowers-=1
                i+=2
            else:
                i+=1

        return numFlowers == 0
                werbed) else -1
            if left != 1 and right != 1:
                numFlowers-=1
                flowerbed[i] = 1
                
        return numFlowers == 0
