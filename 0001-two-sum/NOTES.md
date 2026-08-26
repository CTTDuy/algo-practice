# 1. Two Sum (Easy)

https://leetcode.com/problems/two-sum/

- **Pattern:** flip the question — for each `x`, the partner MUST be `target - x`. Store visited values in a dict `{value: index}` for O(1) lookup. O(n) time, O(n) space.
- **Key detail:** check the dict BEFORE inserting the current element — this is what makes `[3,3], target=6` work without using the same element twice.
- **Python `!` moment (TS):** `seen.get(complement)!` — safe only because `has()` was checked first.
- First problem ever. Started by not knowing where `target` comes from (it's an input parameter — LeetCode calls the function with each test case).
