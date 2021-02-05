# Kadane's aglorithm: https://www.youtube.com/watch?v=58yMrWfUS7k

class Solution:
    def maxSubArray(self, nums: list) -> int:
        total_sum = max_sum = nums[0]

        for i in nums[1:]:
            total_sum = max(i, total_sum+i)
            max_sum = max(max_sum, total_sum)

        return max_sum


solution = Solution()

print(solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
