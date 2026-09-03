class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = {}
        left = 0
        best = 0

        for right, c in enumerate(s):
            if c in last and last[c] >= left:
                left = last[c] + 1

            last[c] = right
            best = max(best, right - left + 1)

        return best


TESTS = [
    ("spec ex1",                   "abcabcbb", 3),
    ("spec ex2 all same",          "bbbbb",    1),
    ("spec ex3 substring not subsequence", "pwwkew", 3),
    ("empty string",               "",         0),
    ("single char",                "a",        1),
    ("two distinct",               "au",       2),
    ("stale-entry trap",           "dvdf",     3),
    ("left must never move back",  "abba",     2),
    ("space counts as a char",     " ",        1),
    ("late repeat of early char",  "tmmzuxt",  5),
]

if __name__ == "__main__":
    sol = Solution()
    failed = 0
    for name, s, expected in TESTS:
        actual = sol.lengthOfLongestSubstring(s)
        ok = actual == expected
        if not ok:
            failed += 1
        print(f"{'PASS' if ok else 'FAIL'}  {name}: f({s!r}) = {actual}, expected {expected}")
    print(f"\n{len(TESTS) - failed}/{len(TESTS)} passed")
