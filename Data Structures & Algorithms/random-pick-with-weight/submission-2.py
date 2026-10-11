import random

class Solution:
    def __init__(self, w: list[int]):
        # 1. 预处理前缀和数组
        self.prefix_sums = []
        cur_sum = 0
        for weight in w:
            cur_sum += weight
            self.prefix_sums.append(cur_sum)
        self.total_sum = cur_sum

    def pickIndex(self) -> int:
        # 2. 生成 [1, total_sum] 范围内的随机整数
        target = random.randint(1, self.total_sum)
        
        # 3. 手写二分查找：寻找第一个 >= target 的位置（bisect_left）
        left, right = 0, len(self.prefix_sums) - 1
        while left < right:
            mid = (left + right) // 2
            if self.prefix_sums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left