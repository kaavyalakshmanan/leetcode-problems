class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # O(n) time O(26) space
        # this is a bit of a tricky strings problem
        # we're given 2 strings, and we want to determine if s2 contains a permutation of s1
        # we're told in the problem that both strings only contain lowercase english letters
        # whenever we're told that, we know our friend ord() will come in handy
        # create a character count array for both s1 and s2, iterate over length of s1, and basically count the number of occurrences of each letter in s1 and s2, to the length of s1
        # iterate over both arrays and count the number of matches so far -- numMatches
        # once thats done, iterate oer the rest of s2, keep track of numMatches and return True if numMatches == 26
        # since this is a sliding window problem, we wont have to iterate over both arrays again
        # instead, our left and right pointers will always be the length of s1, left will result in decrementing, right will result in incrementing
        # when theres a character count match in both arrays, we increment numMatches
        # otherwise, if we are decrementing the left pointer, s1's count could be 1 + s2's count, in which case we decrement numMatches
        # conversely, if we are incrementing the right pointer, s2's count could be 1 + s1's count, in which case we also decrement numMatches
        # basically we want the counts to either be exactly the same or one off

        if len(s1) > len(s2):
            return False

        s1Count = [0] * 26
        s2Count = [0] * 26

        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')]+=1
            s2Count[ord(s2[i]) - ord('a')]+=1

        numMatches = 0
        for idx in range(26):
            if s1Count[idx] == s2Count[idx]:
                numMatches+=1

        left, right = 0, len(s1)

        while right < len(s2):
            if numMatches == 26:
                return True
            leftIdx = ord(s2[left]) - ord('a')
            rightIdx = ord(s2[right]) - ord('a')

            s2Count[leftIdx]-=1
            if s2Count[leftIdx] == s1Count[leftIdx]:
                numMatches+=1
            elif s1Count[leftIdx] - 1 == s2Count[leftIdx]:
                numMatches-=1

            s2Count[rightIdx]+=1
            if s2Count[rightIdx] == s1Count[rightIdx]:
                numMatches+=1
            elif s1Count[rightIdx] + 1 == s2Count[rightIdx]:
                numMatches-=1

            left+=1
            right+=1


            
        return numMatches == 26


        






