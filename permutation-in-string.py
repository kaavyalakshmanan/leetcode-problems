class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # O(n+m) time O(1) space
        # Sliding window

        if len(s1) > len(s2):
            return False
        
        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')]+=1
            s2Count[ord(s2[i]) - ord('a')]+=1

        numMatches = 0
        left, right = 0, len(s1)
        for i in range(len(s2Count)):
            if s2Count[i] == s1Count[i]:
                numMatches+=1

        for i in range(right, len(s2)):
            if numMatches == 26:
                return True
            rightIdx = ord(s2[i]) - ord('a')
            s2Count[rightIdx]+=1
            if s2Count[rightIdx] == 1 + s1Count[rightIdx]:
                numMatches-=1
            elif s2Count[rightIdx] == s1Count[rightIdx]:
                numMatches+=1

            leftIdx = ord(s2[left]) - ord('a')
            s2Count[leftIdx]-=1
            if s2Count[leftIdx] == s1Count[leftIdx]-1:
                numMatches-=1
            elif s2Count[leftIdx] == s1Count[leftIdx]:
                numMatches+=1
            left+=1

        return numMatches == 26

            
