class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        c = Counter(nums)
        c = sorted(c.items(), key = lambda x:x[1], reverse = True)[:k]

        return [a for a, b in c]