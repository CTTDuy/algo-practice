function myAtoi(s: string): number {
    const INT_MAX = 2 ** 31 - 1;
    const INT_MIN = -(2 ** 31);

    let i = 0;

    while (i < s.length && s[i] === ' ') {
        i++;
    }

    let sign = 1;
    if (i < s.length && (s[i] === '+' || s[i] === '-')) {
        if (s[i] === '-') sign = -1;
        i++;
    }

    let result = 0;
    while (i < s.length && s[i] >= '0' && s[i] <= '9') {
        result = result * 10 + Number(s[i]);
        i++;
    }

    return Math.max(INT_MIN, Math.min(INT_MAX, sign * result));
}
