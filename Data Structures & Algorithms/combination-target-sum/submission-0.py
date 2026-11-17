class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        results = []
        path = []

        def backtrack(start, remaining):
            if remaining == 0:
                results.append(path.copy())
                return
            
            for index in range(start, len(nums)):
                number = nums[index]
                if number > remaining:
                    break
                
                path.append(number)
                backtrack(index, remaining - number)
                path.pop()
        
        backtrack(0, target)
        return results