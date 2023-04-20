class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        # O(n^2) time O(n^2) space if we count output array where n = numRows

        res = [[1]]

        for i in range(1, numRows):
            prevArr = res[-1]
            currArr = [0] * (i+1)
            currArr[0], currArr[i] = 1, 1
            j = 1

            while j < len(currArr)-1:
                currArr[j] = prevArr[j] + prevArr[j-1]
                j+=1
            
            res.append(currArr)

        return res


        
