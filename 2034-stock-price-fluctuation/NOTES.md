# 2034. Stock Price Fluctuation (Medium)

https://leetcode.com/problems/stock-price-fluctuation/

- **Pattern:** design problem — one data structure per question. Dict (ts -> price) as **source of truth**, `latest` variable for the newest timestamp, two heaps as **lazy indexes** for max/min.
- **Lazy deletion:** heaps can't update in place, so corrections just push new entries; stale tops are detected (heap top != dict value) and discarded on read. Same idea as tombstones in log-structured storage.
- **Bug I hit #1:** `current()` != `maximum()` — max by TIME vs max by PRICE. The spec example has both side by side (5 vs 10); tracing it first would have caught this.
- **Bug I hit #2:** `self.prices.latest()` — `latest` belongs to `self`, not to the dict, and it's a variable, not a method.
- **Perf measured:** naive scan = 1.91s / 50k calls; heap = 0.01s (~200x). Constraint is 10^5 calls -> naive risks TLE.
- `trace.py` prints object state after every call — how a class keeps memory across calls.
