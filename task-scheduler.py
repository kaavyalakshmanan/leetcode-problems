class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        # Step 1: Create/initialize a maxHeap
        maxHeap = []
        heapq.heapify(maxHeap)

        count = collections.Counter(tasks)
        for k, v in count.items():
            heapq.heappush(maxHeap, v * -1)

        # Step 2: Create a Q
        q = collections.deque([])

        # Step 3: Initialize time 
        time = 0

        # Step 4: Keep going while there's something in the maxHeap
        while maxHeap or q:
            time+=1
            if maxHeap:
                task = heapq.heappop(maxHeap) + 1
                if task < 0:
                    q.append([task, time + n])

            # Check if there's anything in Q to add to maxHeap
            if q and q[0][1] == time:
                task, time = q.popleft() 
                heapq.heappush(maxHeap, task)

        return time
