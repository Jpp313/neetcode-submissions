class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        arr = [[] for i in range(len(nums) + 1)]
        
        for key,val in count.items():
            arr[val].append(key)
        

        res = []
        for num in range(len(arr) - 1, 0 , -1):
            for val in arr[num]:
                res.append(val)
                if len(res) == k:
                    return res