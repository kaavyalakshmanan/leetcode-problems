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
            right = flowerbed[i+1] if i+1 < len(flowerbed) else -1
            if left != 1 and right != 1:
                numFlowers-=1
                flowerbed[i] = 1
                
        return numFlowers == 0
