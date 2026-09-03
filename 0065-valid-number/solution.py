class Solution:
    def isNumber(self, s: str) -> bool:
        seen_digit = False
        seen_dot = False
        seen_exp = False

        for i, c in enumerate(s):
            if c.isdigit():
                seen_digit = True
            elif c in '+-':
                if i > 0 and s[i - 1] not in 'eE':
                    return False
            elif c == '.':
                if seen_dot or seen_exp:
                    return False
                seen_dot = True
            elif c in 'eE':
                if seen_exp or not seen_digit:
                    return False
                seen_exp = True
                seen_digit = False
            else:
                return False

        return seen_digit


VALID = ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3",
         "3e+7", "+6e-1", "53.5e93", "-123.456e789", "46.e3", ".5"]
INVALID = ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53",
           ".", "+", "-", "e", ".e1", "+.", "6+1", "4e+", "."]

if __name__ == "__main__":
    sol = Solution()
    failed = 0
    for s in VALID:
        if not sol.isNumber(s):
            print(f"FAIL  expected True : {s!r}")
            failed += 1
    for s in INVALID:
        if sol.isNumber(s):
            print(f"FAIL  expected False: {s!r}")
            failed += 1
    total = len(VALID) + len(INVALID)
    print(f"{total - failed}/{total} passed")
