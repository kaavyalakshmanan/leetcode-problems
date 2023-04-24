class Solution:
    def partition(self, s: str) -> List[List[str]]:

        # Given a string, we are tasked with partitioning it into palindromes
        # The way to do this is by backtracking
        # Start at each index, and keep going to see what length of palindrome we can get
        # eg --> aab
            # We can either take a, aa, or aab
                # from a we can do a or ab
                    # from a we can only do b
                        # true base case, reached end of length of s, append to some return array --> [a, a, b]
                    # backtrack to ab  
                        # this is not a palindrome, false base case
            # backtrack to aa
                # from here we can only take b
                    # true base case, reached end of length of s, append to some return array --> [aa, b]
            # backtrack to aab
                # this is not a palindrome, false base case

        # so this is technically brute force because we are computing all the possible palindromes

        # O(n*2^n) time and O(n) space

        res = []
        currPart = []

        def backtrack(i):
            if i == len(s):
                res.append(currPart.copy())
                return
            
            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    currPart.append(s[i:j+1])
                    backtrack(j+1)
                    currPart.pop()

        backtrack(0)
        return res

    def isPalindrome(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i+=1
            j-=1

        return True

                

        
