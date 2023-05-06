class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        people.sort()

        # greedy algo
        # sort inoput array, and try to pair heaviest and least heaviest

        # O(nlogn) time O(n) space 
        left, right = 0, len(people)-1
        numBoats = 0
        while left <=right:
            currWeight = people[left] + people[right]
            if currWeight <= limit:
                numBoats+=1
                left+=1
                right-=1
            else:
                numBoats+=1
                right-=1

        return numBoats
