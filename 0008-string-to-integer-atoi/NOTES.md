# 8. String to Integer — atoi (Medium)

https://leetcode.com/problems/string-to-integer-atoi/

- **Pattern:** spec-following with a one-way cursor — 4 sequential stations (skip spaces -> read one sign -> read digits until non-digit -> clamp to 32-bit). No algorithmic insight needed; the 21.7% acceptance is people being sloppy with the spec.
- **Killer case:** `"0-1"` -> 0. The `-` after a digit is NOT a sign — it's a stranger that ends the parse. Signs are only legal before the first digit.
- **Clamp:** compute freely, then `max(INT_MIN, min(INT_MAX, sign * result))`. Python ints are unbounded; JS numbers are exact well past 2^31, so post-clamping is safe in both.
- **Build a number from digits:** `result = result * 10 + digit`.
- ⚠️ **Solution was studied, not self-derived (2026-09-03). Re-solve from scratch ~2026-09-06 without opening this file.**
