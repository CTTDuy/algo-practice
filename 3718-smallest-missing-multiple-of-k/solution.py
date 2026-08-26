from typing import List


class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        seen = set(nums)

        multiple = k
        while multiple in seen:
            multiple += k

        return multiple


TESTS = [
    ("spec ex1 happy path",       [8, 2, 3, 4, 6],    2,   10),
    ("spec ex2 first missing",    [1, 4, 7, 10, 15],  5,   5),
    ("gap in middle",             [3, 6, 12],         3,   9),
    ("answer beyond max(nums)",   [2, 4, 6, 8, 10],   2,   12),
    ("lower boundary all 1s",     [1],                1,   2),
    ("upper boundary all 100s",   [100],              100, 200),
    ("nums has no multiples",     [1, 3, 7, 99],      2,   2),
    ("duplicates",                [5, 5, 5],          5,   10),
    ("k larger than all",         [1, 2, 3],          50,  50),
]

if __name__ == "__main__":
    s = Solution()
    failed = 0
    for name, nums, k, expected in TESTS:
        actual = s.missingMultiple(nums, k)
        ok = actual == expected
        if not ok:
            failed += 1
        print(f"{'PASS' if ok else 'FAIL'}  {name}: got {actual}, expected {expected}")
    print(f"\n{len(TESTS) - failed}/{len(TESTS)} passed")
