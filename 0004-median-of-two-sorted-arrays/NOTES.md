# 4. Median of Two Sorted Arrays (Hard)

https://leetcode.com/problems/median-of-two-sorted-arrays/

- **Pattern: TWO POINTERS (merge)** — first problem of ladder step 2. Two sorted piles, two fingers `i`/`j`; each round take the smaller top card, advance that finger; dump the leftover pile at the end. This merge is also the heart of merge sort.
- Median: odd total -> `merged[n//2]`; even -> average of `merged[n//2 - 1]` and `merged[n//2]`.
- **The stated O(log(m+n)) requirement is not enforced** by the judge — constraints (`m+n <= 2000`) make O(m+n) pass easily. The true O(log) solution (binary search over the partition point) is a famous beast — deliberately NOT studied yet; revisit after the binary search ladder step.
- Python luxuries vs TS: `merged.extend(nums1[i:])` (slice dump) vs an explicit `while` loop; `i = j = 0` chained assignment.
- Solved 2026-09-03 (taught). Self-solve follow-up that uses this exact merge: **21. Merge Two Sorted Lists**.
