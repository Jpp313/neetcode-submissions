class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        freq_dict = {}

        for i in range(len(nums)):
            freq_dict[nums[i]] = 1 + freq_dict.get(nums[i], 0)

        res = [[] for i in range(len(nums) + 1)]

        for key, val in freq_dict.items():
            res[val].append(key)
        
        out = []
        for i in range(len(res) - 1, 0, -1):
            for num in res[i]:
                out.append(num)
                if len(out) == k:
                    return out
           
        