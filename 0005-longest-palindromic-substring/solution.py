class Solution:
    def longestPalindrome(self, s: str) -> str:
        best_start, best_len = 0, 1

        def expand(left: int, right: int):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - left - 1

        for i in range(len(s)):
            for l, r in ((i, i), (i, i + 1)):
                start, length = expand(l, r)
                if length > best_len:
                    best_start, best_len = start, length

        return s[best_start:best_start + best_len]


# The answer can be ambiguous ("bab" vs "aba"), so tests check properties:
# result is a substring, is a palindrome, and has the expected length.
TESTS = [
    ("spec ex1 odd",            "babad",            3),
    ("spec ex2 even center",    "cbbd",             2),
    ("single char",             "a",                1),
    ("two distinct",            "ac",               1),
    ("two same",                "bb",               2),
    ("all same",                "aaaa",             4),
    ("whole string palindrome", "abcba",            5),
    ("even in middle",          "forgeeksskeegfor", 10),
    ("palindrome at edges",     "aacabdkacaa",      3),
    ("digits allowed",          "12321ab",          5),
]

if __name__ == "__main__":
    sol = Solution()
    failed = 0
    for name, s, expected_len in TESTS:
        r = sol.longestPalindrome(s)
        ok = (r in s) and (r == r[::-1]) and (len(r) == expected_len)
        if not ok:
            failed += 1
        print(f"{'PASS' if ok else 'FAIL'}  {name}: f({s!r}) = {r!r} (len {len(r)}, expected len {expected_len})")
    print(f"\n{len(TESTS) - failed}/{len(TESTS)} passed")
