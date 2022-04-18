class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        # O(max(m,n)) time O(m) space
        
        list1Dict = { name: i for i, name in enumerate(list1) }
        minIdxSum = inf
        res = []
        
        for i, name in enumerate(list2):
            if name in list1Dict:
                if (i + list1Dict[name]) < minIdxSum:
                    minIdxSum = (i + list1Dict[name])
                    res = [name]
                elif (i + list1Dict[name]) == minIdxSum:
                    res.append(name)
                
        return res
