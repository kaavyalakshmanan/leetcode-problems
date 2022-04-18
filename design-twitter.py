class Twitter:

    def __init__(self):
        
        # O(k) time O(1) space
        
        self.followersMap = defaultdict(set)
        self.tweetsMap = defaultdict(list)
        
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        
        self.tweetsMap[userId].append([self.time, tweetId])
        self.time-=1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        
        minHeap = []
        res = []
        
        self.followersMap[userId].add(userId)
        
        for followeeId in self.followersMap[userId]:
            if followeeId in self.tweetsMap:
                index = len(self.tweetsMap[followeeId])-1
                time, tweetId = self.tweetsMap[followeeId][index]
                heapq.heappush(minHeap, [time, tweetId, followeeId, index-1])
            
        while len(res) < 10 and minHeap:
            time, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            
            if index >= 0:
                time, tweetId = self.tweetsMap[followeeId][index]
                heapq.heappush(minHeap, [time, tweetId, followeeId, index-1])
                
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        
        self.followersMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        
        if followeeId in self.followersMap[followerId]:
            self.followersMap[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
