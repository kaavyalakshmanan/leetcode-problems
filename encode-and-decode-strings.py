class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """

        # O(n) time O(n) space
        # Use array functions and special char

        res = ""

        for i, s in enumerate(strs):
            res+=s
            if i < len(strs)-1:
                res+='π'

        return res
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """

        res = s.split('π')
        return res
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
