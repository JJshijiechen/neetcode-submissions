# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(minHeap, (node.val, i, node))
                # i means it comes from 0th - kth list

        dummy = ListNode()
        tail = dummy

        while minHeap:
            val, i, node = heapq.heappop(minHeap)

            tail.next = node
            tail = tail.next

            if node.next:
                heapq.heappush(minHeap, (node.next.val, i, node.next))

        return dummy.next