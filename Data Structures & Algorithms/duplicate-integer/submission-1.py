class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        c = {}
        for i in nums:
            if i in c:
                c[i]+=1
            else:
                c[i]=1

        for i in nums:
            if c[i] > 1:
                return True
        return False