# 3. Longest Substring Without Repeating Characters (Medium)

https://leetcode.com/problems/longest-substring-without-repeating-characters/

## Approach — the path to the solution

1. **What is it really asking?** Longest CONTIGUOUS run with no duplicate chars. Substring != subsequence (spec example 3 warns: "pwke" doesn't count).
2. **How would I do it by hand?** Two fingers hugging a stretch of the string; right finger eats chars one by one; on a duplicate, left finger jumps past the old occurrence. The stretch = a **sliding window**.
3. **What question repeats?** "Has this char appeared inside my window — and where?" -> existence + position -> dict `{char: last index}` (Two Sum's notebook, 4th appearance).
4. **What does it resemble?** Two Sum (dict of positions) + 0004 (two pointers) — hybridized: both pointers on ONE string.
5. **Where will I go wrong?** (a) `10^5` constraint -> need O(n), brute O(n^2) too slow; (b) empty string -> 0; (c) spaces are chars (` ` -> 1); (d) **the killer**: a char seen BEFORE the current window is a stale dict entry — guard with `last[c] >= left`, otherwise `"abba"` moves `left` BACKWARD and breaks the window (expected 2).

## Key lines

- `if c in last and last[c] >= left:` — the `>= left` check distinguishes "duplicate inside window" from "stale entry"; without it, `dvdf` and `abba` fail.
- `left = last[c] + 1` — jump, don't crawl: left leaps directly past the old occurrence (this is what makes it one-pass O(n)).
- `best = max(best, right - left + 1)` — measure after every extension.

- **Pattern: SLIDING WINDOW** (ladder step 3) = two pointers on one sequence + a lookup structure describing the window's contents.
- Solved 2026-09-03 (studied, for the doc store). Self-solve follow-up: 121 Best Time to Buy and Sell Stock (simplest sliding-window relative).
