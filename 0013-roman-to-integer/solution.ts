function romanToInt(s: string): number {
    const values = new Map<string, number>([
        ['I', 1], ['V', 5], ['X', 10], ['L', 50],
        ['C', 100], ['D', 500], ['M', 1000],
    ]);

    let total = 0;

    for (let i = 0; i < s.length; i++) {
        const cur = values.get(s[i])!;
        const next = values.get(s[i + 1]) ?? 0; // past end of string -> 0, last char always adds

        if (cur < next) {
            total -= cur;
        } else {
            total += cur;
        }
    }

    return total;
}
