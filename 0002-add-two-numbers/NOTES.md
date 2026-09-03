# 2. Add Two Numbers (Medium)

https://leetcode.com/problems/add-two-numbers/

## Approach — the path to the solution

1. **What is it really asking?** Add two numbers whose digits arrive as linked lists, units digit first.
2. **How would I do it by hand?** Exactly like grade school: add units, write the digit, carry the 1, move left. The "reversed" storage is a GIFT — units are already first, so hand-addition maps 1:1 onto walking both lists.
3. **What question repeats every step?** "Current digit of each list + carry -> what digit do I write, what do I carry?" -> just three variables per step: `l1.val`, `l2.val`, `carry`. No lookup structure needed at all.
4. **What does it resemble?** Walking two sequences in lockstep = the two-pointer merge shape (0004), but on nodes instead of indexes.
5. **Where will I go wrong?** (a) lists of different lengths -> treat a finished list as contributing 0; (b) final carry needs an extra node (`[5]+[5]=[0,1]`) -> loop while `l1 or l2 or carry`; (c) building a NEW list needs somewhere to hang the first node -> dummy head trick.

Dead end I'd hit without step 2: trying to convert lists to ints, add, convert back — works here but overflows in fixed-int languages and misses the whole lesson; the digit-walk is the intended shape.

- **New structure: linked list** — each node = `{val, next}` (a class!). Traverse with `while node: ...; node = node.next` instead of `i++`. Array = numbered seats; linked list = treasure hunt.
- **Insight:** reversed digit order is a GIFT — it's exactly how you add by hand (units first, carry left). Whole problem = grade-school addition with a `carry` variable.
- **Dummy head trick:** start with a throwaway node, append after it, return `dummy.next`. Kills the "first node is special" branch. Memorize — used in most list-building problems.
- **Loop condition `while l1 or l2 or carry`** handles: different lengths (shorter list contributes 0) AND the final carry creating an extra node (`[5]+[5]=[0,1]`).
- `divmod(total, 10)` = (carry, digit) in one call; TS splits into `Math.floor(total/10)` + `total % 10`.
- First linked-list problem (2026-09-03, taught). Follow-ups to self-solve: 206 Reverse Linked List, 21 Merge Two Sorted Lists.
