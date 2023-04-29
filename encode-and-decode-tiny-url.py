class Codec:

    def __init__(self):
        self.map = {}
        self.tiny = "http://tinyurl.com/"
        self.letters = string.ascii_lowercase
    

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """

        hashURL = random.choice(self.letters)
        tinyURL = self.tiny + hashURL

        self.map[tinyURL] = longUrl

        return tinyURL



        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """

        print(shortUrl)
        
        return self.map[shortUrl]


        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
