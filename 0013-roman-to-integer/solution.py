class Solution:
    def romanToInt(self, s: str) -> int:
        values = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                  'C': 100, 'D': 500, 'M': 1000}

        total = 0

        for i in range(len(s)):
            cur = values[s[i]]
            nxt = values[s[i + 1]] if i + 1 < len(s) else 0

            if cur < nxt:
                total -= cur
            else:
                total += cur

        return total


TESTS = [
    ("spec ex1 simple add",    "III",       3),
    ("spec ex2 mixed",         "LVIII",     58),
    ("spec ex3 all subtracts", "MCMXCIV",   1994),
    ("single char",            "I",         1),
    ("pure subtract pair",     "IV",        4),
    ("nine",                   "IX",        9),
    ("forty + nine",           "XLIX",      49),
    ("max value",              "MMMCMXCIX", 3999),
    ("no subtraction at all",  "MDCLXVI",   1666),
]

if __name__ == "__main__":
    sol = Solution()
    failed = 0
    for name, s, expected in TESTS:
        actual = sol.romanToInt(s)
        ok = actual == expected
        if not ok:
            failed += 1
        print(f"{'PASS' if ok else 'FAIL'}  {name}: romanToInt('{s}') = {actual}, expected {expected}")
    print(f"\n{len(TESTS) - failed}/{len(TESTS)} passed")
