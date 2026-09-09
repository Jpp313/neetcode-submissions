class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        countNums = {}
        arr = [[] for i in range(len(nums) + 1)] # filling array with lists for most possible freq char

        for num in nums:
            countNums[num] = 1 + countNums.get(num, 0)
        
        for key, val in countNums.items():
            arr[val].append(key)
        
        res = []
        for i in range(len(arr) - 1, -1 , -1):
            for val in arr[i]:
                res.append(val)
                if len(res) == k:
                    return res
                
