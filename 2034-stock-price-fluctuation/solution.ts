// Submit version. PriorityQueue comes from @datastructures-js/priority-queue,
// preloaded in LeetCode's JS/TS runtime — locally you'd `npm install` it.
class StockPrice {
    private prices = new Map<number, number>();
    private latest = 0;
    private minHeap = new PriorityQueue<[number, number]>((a, b) => a[0] - b[0]); // [price, ts]
    private maxHeap = new PriorityQueue<[number, number]>((a, b) => b[0] - a[0]);

    update(timestamp: number, price: number): void {
        this.prices.set(timestamp, price);
        this.latest = Math.max(this.latest, timestamp);
        this.minHeap.enqueue([price, timestamp]);
        this.maxHeap.enqueue([price, timestamp]);
    }

    current(): number {
        return this.prices.get(this.latest)!;
    }

    maximum(): number {
        while (this.maxHeap.front()![0] !== this.prices.get(this.maxHeap.front()![1])) {
            this.maxHeap.dequeue(); // top was corrected -> stale, discard
        }
        return this.maxHeap.front()![0];
    }

    minimum(): number {
        while (this.minHeap.front()![0] !== this.prices.get(this.minHeap.front()![1])) {
            this.minHeap.dequeue();
        }
        return this.minHeap.front()![0];
    }
}
