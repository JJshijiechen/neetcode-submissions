class Solution:
    def maxFrequency(self, arr: List[int], k: int) -> int:
        ans = arr.count(k)

        for target in set(arr):
            if target == k:
                continue

            cur = 0
            best = 0

            for num in arr:
                if num == target:
                    cur += 1
                elif num == k:
                    cur -= 1

                cur = max(0, cur)
                best = max(best, cur)

            ans = max(ans, arr.count(k) + best)
        return ans