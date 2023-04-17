class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # O(n+m) time O(n+m) space

        if len(t) > len(s):
            return ""

        # Step 1; tDict and sDict
        tDict = {}
        sDict = {}
        for c in t:
            if c not in tDict:
                tDict[c] = 1
                sDict[c] = 0
            else:
                tDict[c]+=1

        have, need = len(tDict), 0
        left, right = 0, 0

        minLen = inf
        leftIdx, rightIdx = -1, -1

        # Step 2: iterate over s
        while right < len(s):
            if s[right] in sDict:
                sDict[s[right]]+=1

                if sDict[s[right]] == tDict[s[right]]:
                    need+=1

                    while have == need:
                        if right-left+1 < minLen:
                            minLen = right-left+1
                            leftIdx = left
                            rightIdx = right
                        if s[left] in sDict:
                            sDict[s[left]]-=1

                            if sDict[s[left]] < tDict[s[left]]:
                                need-=1

                        left+=1

            right +=1

        return s[leftIdx:rightIdx+1]
