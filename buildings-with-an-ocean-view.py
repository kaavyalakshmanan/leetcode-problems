class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        
        # O(n) time O(n) space
        # 2 pointers
        
        output = [len(heights)-1]
        largest = len(heights)-1
        
        for i in range(len(heights)-2, -1, -1):
            if heights[i] > heights[largest]:
                output.append(i)
                largest = i
                
        smallest, largest = 0, len(output)-1
        while smallest < largest:
            output[smallest], output[largest] = output[largest], output[smallest]
            smallest+=1
            largest-=1
            
        
        return output 
            
        
        
