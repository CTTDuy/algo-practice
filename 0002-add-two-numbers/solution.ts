class ListNode {
    val: number;
    next: ListNode | null;
    constructor(val?: number, next?: ListNode | null) {
        this.val = val === undefined ? 0 : val;
        this.next = next === undefined ? null : next;
    }
}

function addTwoNumbers(l1: ListNode | null, l2: ListNode | null): ListNode | null {
    const dummy = new ListNode();
    let cur = dummy;
    let carry = 0;

    while (l1 !== null || l2 !== null || carry > 0) {
        const total = (l1 ? l1.val : 0) + (l2 ? l2.val : 0) + carry;
        carry = Math.floor(total / 10);
        const digit = total % 10;

        cur.next = new ListNode(digit);
        cur = cur.next;

        l1 = l1 ? l1.next : null;
        l2 = l2 ? l2.next : null;
    }

    return dummy.next;
}
// Note: on LeetCode, delete the ListNode class above (they define it) — keep only the function.
