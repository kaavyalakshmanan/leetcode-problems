class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """

        # O(n) time O(n) space

        res = ""
        for i, s in enumerate(strs):
            res += s
            res += "£"

        return res
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """

        # O(n) time O(n) space

        res = s.split("£")
        # if res[-1] == "":
        #     res = res[:-1]

        return res[:-1]
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
