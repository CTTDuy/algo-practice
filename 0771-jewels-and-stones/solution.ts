function numJewelsInStones(jewels: string, stones: string): number {
    const jewelSet = new Set(jewels);

    let count = 0;
    for (const s of stones) {
        if (jewelSet.has(s)) count++;
    }
    return count;
}
