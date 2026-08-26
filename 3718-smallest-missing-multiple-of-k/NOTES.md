# 3718. Smallest Missing Multiple of K (Easy)

https://leetcode.com/problems/smallest-missing-multiple-of-k/

- **Pattern:** walk multiples k, 2k, 3k, ... upward; the first one absent from `nums` is the answer. Repeated existence checks -> dump `nums` into a **set** first (same trick as Two Sum, minus the index).
- **Loop terminates** because `nums[i] <= 100`: any multiple past 100 is guaranteed missing. Re-check this argument if constraints ever widen.
- **Trap case:** `[3,6,12], k=3` -> answer is 9, not 15. A present value AFTER the gap doesn't rescue anything — first hole wins.
- **set vs dict:** need "does it exist?" only -> set. Need "exists + where/what?" -> dict. Set = dict without values.
