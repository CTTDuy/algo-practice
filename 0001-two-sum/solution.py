from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in seen:
                return [seen[complement], i]

            seen[nums[i]] = i

        return []


TESTS = [
    ("spec ex1", [2, 7, 11, 15], 9, [0, 1]),
    ("spec ex2", [3, 2, 4], 6, [1, 2]),
    ("spec ex3 duplicates", [3, 3], 6, [0, 1]),
]

if __name__ == "__main__":
    s = Solution()
    failed = 0
    for name, nums, target, expected in TESTS:
        actual = s.twoSum(nums, target)
        ok = actual == expected
        if not ok:
            failed += 1
        print(f"{'PASS' if ok else 'FAIL'}  {name}: got {actual}, expected {expected}")
    print(f"\n{len(TESTS) - failed}/{len(TESTS)} passed")
