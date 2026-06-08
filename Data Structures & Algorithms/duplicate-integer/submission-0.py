class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for l in range(i + 1, len(nums)):
                if nums[i] == nums[l]: return True
        return False