class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        # O(n) time O(1) space

        maxNum = arr[-1]
        arr[-1] = -1

        for i in range(len(arr)-2, -1, -1):
            tmp = arr[i]
            arr[i] = maxNum
            maxNum = max(maxNum, tmp)

        return arr
