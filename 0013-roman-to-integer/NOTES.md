# 13. Roman to Integer (Easy)

https://leetcode.com/problems/roman-to-integer/

- **Pattern:** hash map (symbol -> value) + **look-ahead one step**: if current value < next value, subtract it (IV, IX, XL, XC, CD, CM); otherwise add. The last char always adds.
- **Boundary handling differs by language:** TS lets `s[i+1]` silently become `undefined`, caught with `?? 0`; Python would raise `IndexError`, so guard with `... if i + 1 < len(s) else 0`. Fail-loud vs fail-silent philosophies.
- **Alternative:** add everything, then subtract 2x for each of the 6 special pairs. Works, but the look-ahead rule is one general law instead of a list of cases.
