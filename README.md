# algo-practice

Practicing algorithms from scratch — every solution ships with its own test suite.

Solutions in Python and TypeScript. Each problem folder contains the solution, a runnable test suite, and a `NOTES.md` with the pattern used and the traps I fell into.

## Problems

| # | Problem | Source | Difficulty | Pattern | Languages |
|---|---------|--------|------------|---------|-----------|
| 1 | [Two Sum](0001-two-sum/) | [LeetCode](https://leetcode.com/problems/two-sum/) | Easy | Hash map — trade memory for lookup speed | Python, TypeScript |
| 2 | [Add Two Numbers](0002-add-two-numbers/) | [LeetCode](https://leetcode.com/problems/add-two-numbers/) | Medium | Linked list traversal + carry + dummy head | Python, TypeScript |
| 4 | [Median of Two Sorted Arrays](0004-median-of-two-sorted-arrays/) | [LeetCode](https://leetcode.com/problems/median-of-two-sorted-arrays/) | Hard | Two pointers — merge two sorted arrays | Python, TypeScript |
| 8 | [String to Integer (atoi)](0008-string-to-integer-atoi/) | [LeetCode](https://leetcode.com/problems/string-to-integer-atoi/) | Medium | Spec-following, one-way cursor, clamp | Python, TypeScript |
| 13 | [Roman to Integer](0013-roman-to-integer/) | [LeetCode](https://leetcode.com/problems/roman-to-integer/) | Easy | Hash map + look-ahead one step | Python, TypeScript |
| 65 | [Valid Number](0065-valid-number/) | [LeetCode](https://leetcode.com/problems/valid-number/) | Hard | Single pass + boolean flags (spec-following) | Python, TypeScript |
| 2034 | [Stock Price Fluctuation](2034-stock-price-fluctuation/) | [LeetCode](https://leetcode.com/problems/stock-price-fluctuation/) | Medium | Dict as source of truth + heaps with lazy deletion | Python, TypeScript |
| 3718 | [Smallest Missing Multiple of K](3718-smallest-missing-multiple-of-k/) | [LeetCode](https://leetcode.com/problems/smallest-missing-multiple-of-k/) | Easy | Set for O(1) existence checks | Python, TypeScript |

## Running the tests

```bash
python3 <problem-folder>/solution.py     # each file self-tests and prints PASS/FAIL
node <problem-folder>/solution.js        # where a JS version exists
```

## Patterns learned so far

- **Existence check inside a loop → build a set/dict first.** `x in list` scans the whole list every time; `x in set` is a hash lookup. Measured: ~5,500x faster at 100k elements.
- **Look-ahead:** compare the current element with the next one to decide the action (Roman numerals' subtraction rule).
- **Source of truth + lazy index:** when a structure can't be updated in place (heap), keep a dict as the truth and discard stale heap tops lazily on read.
