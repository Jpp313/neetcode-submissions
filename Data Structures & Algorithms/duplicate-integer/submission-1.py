class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        no_duplicates = set()
        for val in nums:
            no_duplicates.add(val)

        if len(no_duplicates) < len(nums):
            return True
        else:
            return False