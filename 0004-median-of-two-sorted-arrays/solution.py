from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = []
        i = j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1

        merged.extend(nums1[i:])
        merged.extend(nums2[j:])

        n = len(merged)
        mid = n // 2
        if n % 2 == 1:
            return float(merged[mid])
        return (merged[mid - 1] + merged[mid]) / 2


TESTS = [
    ("spec ex1 odd total",     [1, 3],       [2],        2.0),
    ("spec ex2 even total",    [1, 2],       [3, 4],     2.5),
    ("first array empty",      [],           [1],        1.0),
    ("second array empty",     [2],          [],         2.0),
    ("all equal",              [0, 0],       [0, 0],     0.0),
    ("interleaved",            [1, 3],       [2, 7],     2.5),
    ("negatives",              [-5, -1],     [-3],       -3.0),
    ("no overlap",             [1, 2],       [10, 11],   6.0),
    ("single each",            [1],          [2],        1.5),
]

if __name__ == "__main__":
    sol = Solution()
    failed = 0
    for name, a, b, expected in TESTS:
        actual = sol.findMedianSortedArrays(a, b)
        ok = abs(actual - expected) < 1e-9
        if not ok:
            failed += 1
        print(f"{'PASS' if ok else 'FAIL'}  {name}: median({a}, {b}) = {actual}, expected {expected}")
    print(f"\n{len(TESTS) - failed}/{len(TESTS)} passed")
