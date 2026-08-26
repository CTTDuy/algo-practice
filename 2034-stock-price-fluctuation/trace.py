"""Prints the internal state after every call — run this to SEE how a class
keeps memory across calls (the thing a bare function can't do)."""


class StockPrice:

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


if __name__ == "__main__":
    print("Create object:  obj = StockPrice()")
    obj = StockPrice()
    print(f"   state:  prices={obj.prices}  latest={obj.latest}\n")

    script = [
        ("update", (1, 10)),
        ("update", (2, 5)),
        ("current", ()),
        ("maximum", ()),
        ("update", (1, 3)),
        ("maximum", ()),
        ("update", (4, 2)),
        ("minimum", ()),
    ]

    for method, args in script:
        result = getattr(obj, method)(*args)
        call = f"obj.{method}{args if args else '()'}"
        answer = "null" if result is None else result
        print(f"{call:<22} -> returns: {answer}")
        print(f"   state:  prices={obj.prices}  latest={obj.latest}\n")
