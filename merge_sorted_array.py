class Solution:
    def merge(self, nums1: list, m: int, nums2: list, n: int) -> None:
        nums1[:] = sorted(nums1[:m] + nums2[:n])
