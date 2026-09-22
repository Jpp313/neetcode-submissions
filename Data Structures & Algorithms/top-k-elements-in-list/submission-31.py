class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq_dict = {}

        for num in nums:
            freq_dict[num] = 1 + freq_dict.get(num, 0)

        
        arr = [[] for i in range(len(nums) + 1)]  # i : freq v: val

        for key,val in freq_dict.items():
            arr[val].append(key)
        
        res = []

        for i in range(len(arr) - 1, 0, -1):
            for num in arr[i]:
                res.append(num)
                if len(res) == k:
                    return res

