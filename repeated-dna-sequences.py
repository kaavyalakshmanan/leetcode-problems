class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:

        # O(n) time O(n) space

        if len(s) <= 10:
            return []

        sequences = set()
        res = set()

        # set up our pointers
        left, right = 0, 9

        while right < len(s):
            if s[left:right+1] in sequences:
                res.add(s[left:right+1])
            else:
                sequences.add(s[left:right+1])
            left+=1
            right+=1

        return list(res)



        

