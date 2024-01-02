class Codec:

    # O(n) time O(n) space
    # Iterate over string
    
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """

        res = ""

        for i, s in enumerate(strs):
            res+=s
            if i < len(strs)-1:
                res+="£"
            

        return res
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """

        sArr = s.split("£")
        return sArr
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
