class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        prevMap = {}

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in prevMap.keys():
                return [prevMap[diff],i]
            prevMap[nums[i]] = i
        

        