class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        # O(min(m,n) * (m+n)) time O(min(m,n)) space because in the while loop we are building
        # str1 and str2

        if len(str2) < len(str1):
            str1, str2 = str2, str1
        len1, len2 = len(str1), len(str2)
        i = len(str1)-1
        
        while i >= 0:
            if len1 % (i+1) and len2 % (i+1):
                i-=1
            else:
                num1 = len1//(i+1)
                num2 = len2//(i+1)
                str3 = str1[:i+1] * num1
                str4 = str1[:i+1] * num2
                if str3 != str1 or str4 != str2:
                    i-=1
                else:
                    return str1[:i+1]

        return ""


            
        
    
