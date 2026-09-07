function longestPalindrome(s: string): string {
    let bestStart = 0;
    let bestLen = 1;

    const expand = (left: number, right: number): void => {
        while (left >= 0 && right < s.length && s[left] === s[right]) {
            left--;
            right++;
        }
        const length = right - left - 1;
        if (length > bestLen) {
            bestLen = length;
            bestStart = left + 1;
        }
    };

    for (let i = 0; i < s.length; i++) {
        expand(i, i);
        expand(i, i + 1);
    }

    return s.slice(bestStart, bestStart + bestLen);
}
