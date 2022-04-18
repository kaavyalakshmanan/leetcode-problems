class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        
        # O(n) time O(n) space
        
        restaurantIds = []
        
        for resto in restaurants:
            if veganFriendly and not resto[2]:
                continue
            if resto[3] > maxPrice:
                continue
            if resto[4] > maxDistance:
                continue
            restaurantIds.append((resto[1], resto[0]))
            
        res = []
        restaurantIds.sort(reverse = True)
        
        for rating, restoId in restaurantIds:
            res.append(restoId)
            

        return res
