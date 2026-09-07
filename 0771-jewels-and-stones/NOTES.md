# 771. Jewels and Stones (Easy)

https://leetcode.com/problems/jewels-and-stones/

## Approach — the path to the solution

1. **What is it really asking?** Count how many chars of `stones` appear in `jewels`. Case-sensitive.
2. **By hand?** Pick up each stone, glance at the "which types are jewels" board, tally.
3. **Repeating question?** "Is this char in jewels?" — pure existence, no position -> **set** (not dict).
4. **Resembles?** The purest form of the hash-set pattern — Two Sum minus the complement, Missing Multiple minus the loop. Constraint gifts "all jewels unique" (no dedup worry).
5. **Where to go wrong?** Almost nowhere — only case-sensitivity (`"z"` vs `"ZZ"` -> 0). `<= 50` means speed is a non-issue; the set is habit, not necessity.

## Notes

- Python idiom: **count with sum** — `sum(s in jewel_set for s in stones)`; each True contributes 1.
- TS: `new Set(jewels)` builds a char set straight from a string; `for..of` iterates chars (never `for..in` — that walks indexes).
- Solved 2026-09-03 (studied, doc store). This is exactly the difficulty tier of a first self-solve.
