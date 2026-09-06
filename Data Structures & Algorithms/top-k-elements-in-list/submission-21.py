class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        freq_dict = {}

        for i in range(len(nums)):
            freq_dict[nums[i]] = 1 + freq_dict.get(nums[i], 0)

        res = [0] * (len(nums) + 1) # to sort freq pairs as freq as index and key as val
        for key, val in freq_dict.items():
            res[val] = key
        # allows to use list indices as sorting from back to front of most frequent elements
        out = []
        for i in range(len(res) - 1, 0, -1):
            if res[i] == 0:
                continue
            if len(out) == k:
                return out
            out.append(res[i])
        return out