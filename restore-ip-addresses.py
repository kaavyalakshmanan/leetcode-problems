class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        # given input string, return an array containing all possbile valid IP addresses
        # a valid IP address doesn't have leading 0s, is between 0 and 255 inclusive, and contains 4 integers deparated by a dot

        # the first idea that comes to mind is a brute force backtracking approach
        # typically backtracking can be optimized using DP/memoization
        # however for this problem, that actually won't work because in this problem we have to construct the IP addresses, we aren't counting the number of ways the IP addresses can be constructed or creating combinations
        # hence we use backtracking 

        # O(m*n) space

        res = []
        if len(s) > 12:
            return res

        def backtrack(i, numDots, currIP):

            # Base cases
            if i == len(s) and numDots == 4:
                # Remove the last dot since we only need 3
                res.append(currIP[:-1])
                return 

            if numDots > 4:
                return

            # we do min here in case i+3 is out of bounds
            for j in range(i, min(i+3, len(s))):
                # i tells us where we begin and j tells us where we end in s
                # can't have leading 0s
                if int(s[i:j+1]) < 256 and (i==j or s[i] != '0'):
                    backtrack(j+1, numDots+1, currIP+s[i:j+1]+".")

  

        backtrack(0, 0, "")
        return res
