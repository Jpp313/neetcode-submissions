class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq_nums = {}

        for val in nums:
            freq_nums[val] = 1 + freq_nums.get(val,0)
        
        arr = [[] for i in range(len(nums) + 1)]

        for key,val in freq_nums.items():
            arr[val].append(key)
        
        res = []
        for number in range(len(arr) - 1, 0, -1):
            for i in arr[number]:
                res.append(i)
                if len(res) == k:
                    return res