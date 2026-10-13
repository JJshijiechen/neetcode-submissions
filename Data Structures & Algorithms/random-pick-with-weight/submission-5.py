class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sums = []
        cur_sum = 0
        for wgt in w:
            cur_sum += wgt
            self.prefix_sums.append(cur_sum)

    def pickIndex(self) -> int:
        target = random.randint(1, self.prefix_sums[-1])
        l, r = 0, len(self.prefix_sums) - 1
        while l < r:
            mid = (l + r) // 2
            if self.prefix_sums[mid] < target:
                l = mid + 1
            else:
                r = mid
        return l

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()