class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for el in nums:
            if el not in count.keys():
                count[el] = 1
            else:
                count[el] += 1

        count = {v: k for k, v in count.items()}
        max_count = max(count.keys())

        return count.get(max_count)
