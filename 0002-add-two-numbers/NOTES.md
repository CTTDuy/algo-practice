# 2. Add Two Numbers (Medium)

https://leetcode.com/problems/add-two-numbers/

- **New structure: linked list** — each node = `{val, next}` (a class!). Traverse with `while node: ...; node = node.next` instead of `i++`. Array = numbered seats; linked list = treasure hunt.
- **Insight:** reversed digit order is a GIFT — it's exactly how you add by hand (units first, carry left). Whole problem = grade-school addition with a `carry` variable.
- **Dummy head trick:** start with a throwaway node, append after it, return `dummy.next`. Kills the "first node is special" branch. Memorize — used in most list-building problems.
- **Loop condition `while l1 or l2 or carry`** handles: different lengths (shorter list contributes 0) AND the final carry creating an extra node (`[5]+[5]=[0,1]`).
- `divmod(total, 10)` = (carry, digit) in one call; TS splits into `Math.floor(total/10)` + `total % 10`.
- First linked-list problem (2026-09-03, taught). Follow-ups to self-solve: 206 Reverse Linked List, 21 Merge Two Sorted Lists.
