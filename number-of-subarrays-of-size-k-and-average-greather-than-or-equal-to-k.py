class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        # O(n) time O(1) space

        # set up
        left, right = 0, 0
        prefixSum = 0
        count = 0

        while right < k-1:
            prefixSum += arr[right]
            right+=1

        while right < len(arr):
            prefixSum += arr[right]
            avg = prefixSum/k
            if avg >= threshold:
                count+=1
            prefixSum -= arr[left]
            left+=1
            right+=1

        return count


