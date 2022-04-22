class Solution:
    def compress(self, chars: List[str]) -> int:
        
        # O(n) time O(1) space
        
        i = 0
        j = 0
        count = 1
        
        while i < len(chars):
            while i+1 < len(chars) and chars[i] == chars[i+1]:
                count+=1
                i+=1
            chars[j] = chars[i]
            j+=1
            if count == 1:
                i+=1
                continue
            else:
                for c in str(count):
                    if j < len(chars):
                        chars[j] = c
                    j+=1
                count = 1
                i+=1
        
        chars = chars[:j]
        return len(chars)
            
            
