function lengthOfLongestSubstring(s: string): number {
    const last = new Map<string, number>();
    let left = 0;
    let best = 0;

    for (let right = 0; right < s.length; right++) {
        const c = s[right];
        const prev = last.get(c);

        if (prev !== undefined && prev >= left) {
            left = prev + 1;
        }

        last.set(c, right);
        best = Math.max(best, right - left + 1);
    }

    return best;
}
