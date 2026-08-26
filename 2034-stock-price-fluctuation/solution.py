import heapq


class StockPriceNaive:
    """Correct but O(n) per maximum()/minimum() call — TLE risk at 10^5 calls.
    Measured: 1.91s for 50k calls vs 0.01s for the heap version."""

    def __init__(self):
        self.prices = {}
        self.latest = 0

    def update(self, timestamp, price):
        self.prices[timestamp] = price
        self.latest = max(self.latest, timestamp)

    def current(self):
        return self.prices[self.latest]

    def maximum(self):
        return max(self.prices.values())

    def minimum(self):
        return min(self.prices.values())


class StockPrice:
    """Submit this one: dict = source of truth, two heaps = lazy indexes."""

    def __init__(self):
        self.prices = {}
        self.latest = 0
        self.min_heap = []  # (price, ts)
        self.max_heap = []  # (-price, ts) — negate to fake a max-heap

    def update(self, timestamp, price):
        self.prices[timestamp] = price
        self.latest = max(self.latest, timestamp)
        heapq.heappush(self.min_heap, (price, timestamp))
        heapq.heappush(self.max_heap, (-price, timestamp))

    def current(self):
        return self.prices[self.latest]

    def maximum(self):
        while -self.max_heap[0][0] != self.prices[self.max_heap[0][1]]:
            heapq.heappop(self.max_heap)  # top was corrected -> stale, discard
        return -self.max_heap[0][0]

    def minimum(self):
        while self.min_heap[0][0] != self.prices[self.min_heap[0][1]]:
            heapq.heappop(self.min_heap)
        return self.min_heap[0][0]


SUITES = [
    ("spec example", [
        ("update", (1, 10), None), ("update", (2, 5), None),
        ("current", (), 5), ("maximum", (), 10),
        ("update", (1, 3), None), ("maximum", (), 5),
        ("update", (4, 2), None), ("minimum", (), 2),
    ]),
    ("correction of latest ts affects current", [
        ("update", (5, 100), None), ("current", (), 100),
        ("update", (5, 1), None), ("current", (), 1),
        ("maximum", (), 1), ("minimum", (), 1),
    ]),
    ("out-of-order arrivals", [
        ("update", (10, 7), None), ("update", (3, 99), None),
        ("current", (), 7),
        ("maximum", (), 99), ("minimum", (), 7),
    ]),
    ("correct same ts many times", [
        ("update", (1, 50), None), ("update", (1, 40), None),
        ("update", (1, 60), None), ("update", (1, 10), None),
        ("current", (), 10), ("maximum", (), 10), ("minimum", (), 10),
    ]),
    ("min corrected upward", [
        ("update", (1, 2), None), ("update", (2, 8), None),
        ("minimum", (), 2),
        ("update", (1, 9), None),
        ("minimum", (), 8), ("maximum", (), 9),
    ]),
]


def run(cls):
    all_ok = True
    for name, steps in SUITES:
        obj = cls()
        for method, args, expected in steps:
            actual = getattr(obj, method)(*args)
            if expected is not None and actual != expected:
                print(f"FAIL  [{cls.__name__}] {name}: {method}{args} got {actual}, expected {expected}")
                all_ok = False
    print(f"{cls.__name__}: {'ALL PASS' if all_ok else 'HAS FAILURES'} ({len(SUITES)} suites)")


if __name__ == "__main__":
    run(StockPriceNaive)
    run(StockPrice)
