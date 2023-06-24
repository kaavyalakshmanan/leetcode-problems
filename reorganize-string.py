class Solution:
    def reorganizeString(self, s: str) -> str:

        # the general idea: keep putting down the current most frequent charactrer
        # the best way to do this is to use a maxHeap where the maxHeap contains the most frequent character
        # the catch: in python we have to implement a maxHeap using a minHeap

        # O(nlogn) time O(n) space

        # Step 1: get the count of each character in s
        count = collections.Counter(s)

        # Step 2: implement maxHeap using a minHeap
        maxHeap = [ [-ct, char] for char, ct in count.items() ]
        heapq.heapify(maxHeap)

        # Step 3: Build res string
        res = ""
        prev = None

        # we want the most frequent character, except the prev character
        while maxHeap or prev:

            # this is how we know we have to return ""
            # this means that we just put down prev and there's nothing left in maxHeap, which means prev is being duplicated
            if prev and not maxHeap:
                return ""

            maxCount, maxChar = heapq.heappop(maxHeap)
            res += maxChar
            
            maxCount+=1
            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            if maxCount != 0:
                prev = [maxCount, maxChar]   

        return res
