class Solution:
    def reverseWords(self, s: str) -> str:
        
        # O(n) time O(n) space
        
        sArray = s.split(" ")
        sArray = sArray[::-1]
        i = len(sArray)-1
        while i >= 0 and sArray[i] == "":
            i-=1
        sArray = sArray[:i+1]
            
        res = ""
        for i, word in enumerate(sArray):
            if word == "":
                continue
            res += word
            if i < len(sArray)-1:
                res+=" "
        
        return res
