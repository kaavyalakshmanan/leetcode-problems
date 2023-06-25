class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:

        # O(n*m) time O(1) space

        length = len(strs[0])
        numDelete = 0
        for i in range(length):
            prevChar = 'a'
            for j in range(len(strs)):
                if (ord(prevChar) - ord(strs[j][i])) <= 0:
                    prevChar = strs[j][i]
                else:
                    numDelete+=1
                    break

        return numDelete
