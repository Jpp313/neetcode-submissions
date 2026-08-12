class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        no_duplicates = set(nums)
        if len(no_duplicates) < len(nums):
            return True
        return False