class Codec:
    
    # O(n) time O(1) space
    # Non ASCII delimeter
    
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        
        output = ""
        for i, a in enumerate(strs):
            output+=a
            if i < len(strs)-1:
                output+='\xa3'
        return output

    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
    
        s = s.split('\xa3')
        return s


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
