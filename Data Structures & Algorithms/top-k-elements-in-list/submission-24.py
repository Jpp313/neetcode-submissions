class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        freq_dict = defaultdict(list)

        for i in range(len(nums)):
            freq_dict[nums[i]] = 1 + freq_dict.get(nums[i], 0)

        res = [0] * (len(nums) + 1)

        for key, val in freq_dict.items():
            res.append(key)
        out = []
        for i in range(len(res) - 1, 0, -1):
            if res[i] == 0:
                continue
            if len(out) == k:
                return out
            out.append(res[i])
        return out