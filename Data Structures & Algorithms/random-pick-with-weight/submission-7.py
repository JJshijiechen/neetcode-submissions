class Solution:

    def __init__(self, w: List[int]):

        self.curSum = 0
        self.preSum = []
        for wgt in w:
            self.curSum += wgt
            self.preSum.append(self.curSum)

    def pickIndex(self) -> int:
        target = random.randint(1, self.preSum[-1])
        l, r = 0, len(self.preSum) - 1
        while l < r:
            m = (l +r) // 2
            if self.preSum[m] < target:
                l = m + 1
            else:
                r = m
        return r



        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()