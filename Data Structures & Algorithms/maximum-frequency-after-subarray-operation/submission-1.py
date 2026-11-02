class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        cntK = nums.count(k)
        res = 0

        for i in set(nums):
            if i == k:
                continue
            cnt = 0
            for num in nums:
                if num == i:
                    cnt += 1
                if num == k:
                    cnt -= 1
                cnt = max(cnt, 0)
                res = max(res, cntK + cnt)
        return res