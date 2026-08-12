class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq_nums = {}
        arr = [[] for i in range(len(nums) + 1)]

        for i in range(len(nums)):
            freq_nums[nums[i]] = 1 + freq_nums.get(nums[i],0)
        
        for num, cnt in freq_nums.items():
            arr[cnt].append(num)
        
        res = []
        for i in range(len(arr) - 1, 0, -1):
            for num in arr[i]:
                res.append(num)
                if len(res) == k:
                    return res




        
