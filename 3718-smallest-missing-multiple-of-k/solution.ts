function missingMultiple(nums: number[], k: number): number {
    const seen = new Set<number>(nums);

    let m = k;
    while (seen.has(m)) {
        m += k;
    }

    return m;
}
