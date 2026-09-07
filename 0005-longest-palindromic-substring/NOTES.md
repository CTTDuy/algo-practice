# 5. Longest Palindromic Substring (Medium)

https://leetcode.com/problems/longest-palindromic-substring/

## Approach — the path to the solution

1. **What is it really asking?** Longest contiguous substring that reads the same both ways. Return the SUBSTRING itself (`-> str`), not the length.
2. **By hand?** Eyes don't scan every substring — they find a CENTER of symmetry and grow outward while both sides match. Flip the question from passive ("is this substring a palindrome?") to active ("how far does the palindrome centered HERE stretch?").
3. **Repeating question?** "Do the chars on both sides still match?" -> two pointers `left--/right++`. No lookup structure needed.
4. **Resembles?** Two pointers (0004), new gait: instead of marching in lockstep over two arrays, the pointers SPREAD APART from one point. Same family, different motion.
5. **Where to go wrong?** (a) ⭐ even-length palindromes have their center BETWEEN two chars (`"bb"` in `"cbbd"`) -> every index needs TWO centers: `(i,i)` odd and `(i,i+1)` even — spec example 2 exists to catch this; (b) after the expand loop both pointers have overshot by one -> real span is `s[left+1 : right]`, length `right-left-1` (off-by-one trap #2); (c) constraint `<= 1000` -> O(n^2) = 10^6 fine; Manacher's O(n) exists but is out-of-tier.

## Key lines

- `for (i,i) and (i,i+1)` — 2n-1 possible centers, all covered.
- `return left + 1, right - left - 1` — undo the overshoot.
- Answer ambiguity ("bab"/"aba" both valid) -> tests check PROPERTIES (is substring + is palindrome + expected length) instead of exact strings — QA note: property-based checks beat exact-match when the spec allows multiple answers.

- **Pattern: EXPAND AROUND CENTER** (two-pointer variant).
- Solved 2026-09-07 (studied, doc store). Related follow-ups: 647 Palindromic Substrings (same expand, just count), 125 Valid Palindrome (pointers moving INWARD — the third gait).
