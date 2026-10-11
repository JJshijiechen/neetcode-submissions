class Solution:

    def __init__(self, w: List[int]):
        self.prefix = [w[0]]
        for i in range(1, len(w)):
            self.prefix.append(self.prefix[-1] + w[i])

    def pickIndex(self) -> int:
        target = random.randint(1, self.prefix[-1])


        l, r = 0, len(self.prefix) - 1
        while l < r:
            mid = (l + r) >> 1
            if self.prefix[mid] < target:
                l = mid + 1
            else:
                r = mid
        return l


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()