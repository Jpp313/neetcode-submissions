class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}

        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        

        arr = [[] for i in range(len(nums) + 1)]
        for key,val in freq.items():
            arr[val].append(key)

        res = []
        for i in range(len(arr) - 1, 0 , -1):
            for num in arr[i]:
                res.append(num)
                if len(res) == k:
                    return res