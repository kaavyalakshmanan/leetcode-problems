class Twitter:

    def __init__(self):
        
        # O(n) time O(n) space
        
        self.tweets = defaultdict(list)
        self.users = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        
        self.tweets[userId].append([self.time, tweetId])
        self.time-=1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        
        minHeap = []
        res = []
        self.users[userId].add(userId)
        
        for followee in self.users[userId]:
            if followee in self.tweets:
                index = len(self.tweets[followee])-1
                time, tweet = self.tweets[followee][index]
                minHeap.append([time, tweet, followee, index-1])
                
        heapq.heapify(minHeap)
                
        while minHeap and len(res) < 10:
            time, tweet, followee, index = heapq.heappop(minHeap)
            res.append(tweet)
            if index >= 0:
                newTime, newTweet = self.tweets[followee][index]
                heapq.heappush(minHeap, [newTime, newTweet, followee, index-1])
                
        return res
         

    def follow(self, followerId: int, followeeId: int) -> None:
        
        self.users[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        
        if followeeId in self.users[followerId]:
            self.users[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
