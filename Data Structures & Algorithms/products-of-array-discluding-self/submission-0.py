class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = []
        for i in range(len(nums)):
            p = 1
            for j in range(len(nums)):
                if j != i:
                    p = p*nums[j]
            l.append(p)
        return l

