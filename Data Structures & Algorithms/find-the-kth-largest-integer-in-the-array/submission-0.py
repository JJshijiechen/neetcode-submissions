import heapq
class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        heap = []
        for num in nums:
            heapq.heappush(heap, (len(num), num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return heapq.nsmallest(1, heap)[0][1]
