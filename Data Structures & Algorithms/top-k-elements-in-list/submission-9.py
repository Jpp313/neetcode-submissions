class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq_nums = {}

        for i in range(len(nums)):
            freq_nums[nums[i]] = 1 + freq_nums.get(nums[i],0)
        
        arr = []
        for num, cnt in freq_nums.items():
            arr.append([cnt,num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res

