class Solution:
    def compress(self, chars: List[str]) -> int:

        # O(n) time O(1) space

        left, right = 0, 0
        while right < len(chars):
            prevChar, prevIdx = chars[right], right
            while right < len(chars) and chars[right] == prevChar:
                right+=1
            count = right - prevIdx
            chars[left] = prevChar
            left+=1
            countStr = str(count)
            digitRight = left + len(countStr)-1
            if count == 1:
                continue
            while count > 0:
                chars[digitRight] = str(count % 10)
                count = count // 10
                digitRight-=1
                left+=1

        return left


        
