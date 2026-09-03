class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -(2**31)

        i = 0
        n = len(s)

        while i < n and s[i] == ' ':
            i += 1

        sign = 1
        if i < n and s[i] in '+-':
            if s[i] == '-':
                sign = -1
            i += 1

        result = 0
        while i < n and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1

        return max(INT_MIN, min(INT_MAX, sign * result))


TESTS = [
    ("spec ex1 plain",           "42",             42),
    ("spec ex2 spaces+sign+zeros", " -042",        -42),
    ("spec ex3 stops at letter", "1337c0d3",       1337),
    ("spec ex4 dash after digit", "0-1",           0),
    ("spec ex5 starts with word", "words and 987", 0),
    ("decimal point stops",      "3.14159",        3),
    ("sign only",                "+",              0),
    ("minus only",               "-",              0),
    ("empty string",             "",               0),
    ("spaces only",              "   ",            0),
    ("double sign",              "+-12",           0),
    ("space between sign+digit", "   +0 123",      0),
    ("clamp below INT_MIN",      "-91283472332",   -2147483648),
    ("clamp above INT_MAX",      "91283472332",    2147483647),
    ("exact INT_MAX",            "2147483647",     2147483647),
    ("exact INT_MIN",            "-2147483648",    -2147483648),
]

if __name__ == "__main__":
    sol = Solution()
    failed = 0
    for name, s, expected in TESTS:
        actual = sol.myAtoi(s)
        ok = actual == expected
        if not ok:
            failed += 1
        print(f"{'PASS' if ok else 'FAIL'}  {name}: myAtoi({s!r}) = {actual}, expected {expected}")
    print(f"\n{len(TESTS) - failed}/{len(TESTS)} passed")
