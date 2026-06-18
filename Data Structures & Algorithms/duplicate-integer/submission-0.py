class Solution:
    from collections import Counter
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq_nums = dict(Counter(nums))
        
        for freq in freq_nums.values():
            if freq > 1:
                return True

        return False