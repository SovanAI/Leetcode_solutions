from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        arr = nums1 + nums2
        arr.sort()

        n = len(arr)
        mid = n // 2

        if n % 2 == 0:
            return (arr[mid - 1] + arr[mid]) / 2
        else:
            return float(arr[mid])