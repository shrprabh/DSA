class Codec:
    def __init__(self):
        self.encodeMap={}
        self.decodeMap={}
        self.baseUrl="http://tinyurl.com/"
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        if longUrl not in self.encodeMap:
            self.encodeMap[longUrl]=self.baseUrl+str(len(longUrl))
            self.decodeMap[self.baseUrl+str(len(longUrl))]=longUrl
        return self.encodeMap[longUrl]
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        print(shortUrl)
        return self.decodeMap[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
    
codec = Codec()
res=codec.decode(codec.encode("https://leetcode.com/problems/design-tinyurl "))
print(res)