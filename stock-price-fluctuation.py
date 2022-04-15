from sortedcontainers import SortedDict

class StockPrice:
    
    # O(n) time O(n) space

    def __init__(self):
        
        self.stocks = {}
        self.timeToPrice = SortedDict()
        self.priceToTime = SortedDict()
        

    def update(self, timestamp: int, price: int) -> None:
        
        if timestamp not in self.stocks:
            self.stocks[timestamp] = price
            
            self.timeToPrice[(timestamp, price)] = None
            self.priceToTime[(price, timestamp)] = None
            
        else:
            prevPrice = self.stocks[timestamp]
            self.stocks[timestamp] = price
            
            del self.timeToPrice[(timestamp, prevPrice)]
            self.timeToPrice[(timestamp, price)] = None
            
            del self.priceToTime[(prevPrice, timestamp)]
            self.priceToTime[(price, timestamp)] = None
        

    def current(self) -> int:
        
    
        return self.timeToPrice.peekitem(-1)[0][1]
        

    def maximum(self) -> int:
        return self.priceToTime.peekitem(-1)[0][0]

    def minimum(self) -> int:
        return self.priceToTime.peekitem(0)[0][0]


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
