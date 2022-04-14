# class Solution:
#     def maxRepeating(self, seq: str, word: str) -> int:
        
#         count = 0
#         while True:
#             x = word * count
#             if word * count not in seq:
#                 return count - 1 
#             count +=1
class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        if word not in sequence:
            return 0

        left = 1
        right = len(sequence) // len(word)
        while left <= right:
            mid = (left + right) // 2
            if word * mid in sequence:
                left = mid + 1
            else:
                right = mid - 1 
                
        return left - 1
