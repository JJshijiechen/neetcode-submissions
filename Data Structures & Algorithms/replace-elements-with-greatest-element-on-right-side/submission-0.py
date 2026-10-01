class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        rightMax = -1
        ans = [0] * n
        for i in range(n - 1, -1, -1):
            ans[i] = rightMax
            rightMax = max(arr[i], rightMax)
        return ans
