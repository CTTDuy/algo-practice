class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_set = set(jewels)
        return sum(s in jewel_set for s in stones)


TESTS = [
    ("spec ex1",              "aA", "aAAbbbb", 3),
    ("spec ex2 case matters", "z",  "ZZ",      0),
    ("all stones are jewels", "ab", "abab",    4),
    ("no stones match",       "c",  "ab",      0),
    ("single char both",      "a",  "a",       1),
    ("stones repeat heavily", "A",  "AAAAA",   5),
]

if __name__ == "__main__":
    sol = Solution()
    failed = 0
    for name, jewels, stones, expected in TESTS:
        actual = sol.numJewelsInStones(jewels, stones)
        ok = actual == expected
        if not ok:
            failed += 1
        print(f"{'PASS' if ok else 'FAIL'}  {name}: f({jewels!r}, {stones!r}) = {actual}, expected {expected}")
    print(f"\n{len(TESTS) - failed}/{len(TESTS)} passed")
