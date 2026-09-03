class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        cur = dummy
        carry = 0

        while l1 or l2 or carry:
            total = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry, digit = divmod(total, 10)

            cur.next = ListNode(digit)
            cur = cur.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next


def to_list(arr):
    dummy = ListNode()
    cur = dummy
    for v in arr:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def to_array(node):
    out = []
    while node:
        out.append(node.val)
        node = node.next
    return out


TESTS = [
    ("spec ex1 342+465=807",   [2, 4, 3],                [5, 6, 4],    [7, 0, 8]),
    ("spec ex2 zeros",         [0],                      [0],          [0]),
    ("spec ex3 carry ripple",  [9, 9, 9, 9, 9, 9, 9],    [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]),
    ("different lengths",      [1, 8],                   [0],          [1, 8]),
    ("carry creates new node", [5],                      [5],          [0, 1]),
    ("carry chains through",   [9, 9],                   [1],          [0, 0, 1]),
]

if __name__ == "__main__":
    sol = Solution()
    failed = 0
    for name, a, b, expected in TESTS:
        actual = to_array(sol.addTwoNumbers(to_list(a), to_list(b)))
        ok = actual == expected
        if not ok:
            failed += 1
        print(f"{'PASS' if ok else 'FAIL'}  {name}: {a} + {b} = {actual}, expected {expected}")
    print(f"\n{len(TESTS) - failed}/{len(TESTS)} passed")
