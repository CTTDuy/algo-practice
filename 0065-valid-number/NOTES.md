# 65. Valid Number (Hard)

https://leetcode.com/problems/valid-number/

- **Pattern:** single pass + 3 boolean flags (`seen_digit`, `seen_dot`, `seen_exp`). For each char ask only "are you legal RIGHT NOW given the flags". Sibling of atoi — "Hard" means spec-fiddly, not idea-hard.
- **The gem:** on `e`, RESET `seen_digit = False` — the exponent now "owes" a digit. Final `return seen_digit` then rejects `"1e"`, `"e3"`, `"."`, `"+"` all at once.
- **Sign rule:** `+/-` legal only at index 0 or immediately after `e/E` — one lookback `s[i-1] in 'eE'` encodes it.
- **Dot rules:** at most one, and never after `e` (exponent must be an integer) — `seen_dot or seen_exp` covers both.
- **Grammar in one line:** `[sign] digits [. digits] [e/E [sign] digits]`, mantissa needs >=1 digit somewhere (`"4."`, `".9"` valid).
- ⚠️ **Studied after surrender (2026-09-03), no self-attempt pasted. Re-solve from scratch together with atoi ~2026-09-06. This one COUNTS as the atoi re-solve exam only if self-derived.**
