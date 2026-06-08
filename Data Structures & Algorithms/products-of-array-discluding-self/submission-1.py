class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i, n in enumerate(nums):
            prod_rest = 1
            for j, m in enumerate(nums):
                if j == i:
                    continue
                prod_rest *= m
            res.append(prod_rest)
        return res