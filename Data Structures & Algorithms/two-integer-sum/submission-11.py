class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = []

        for n in range(len(nums)):
            diff = target - nums[n]

            if diff in seen:
                return [seen.index(diff),n]

            seen.append(nums[n])
