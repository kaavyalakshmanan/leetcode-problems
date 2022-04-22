class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        
        # O(n*2^n) time O(n*2^n) space
        # Backtrack
        
        def backtrack(idx, curr):
            if idx == len(s):
                output.append(curr)
                return
            
            if s[idx].isalpha():
                lower = s[idx].lower()
                upper = s[idx].upper()
                backtrack(idx+1, curr+lower)
                backtrack(idx+1, curr+upper)
                
            else:
                curr+=s[idx]
                backtrack(idx+1, curr)
                
            
        
        output = []
        
        backtrack(0, "")
        
        return output 
