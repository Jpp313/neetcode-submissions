class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq_dict = {}

        for num in nums:
            freq_dict[num] = 1 + freq_dict.get(num,0)
        

        
        arr = [[] for i in range(len(nums) + 1)]
       
        for key, val in freq_dict.items():
            arr[val].append(key)


        res = []

        for i in range(len(arr) - 1, -1, -1):
            if arr[i]:
                for num in arr[i]:
                    res.append(num)
                    if len(res) == k:
                        return res
