# Pattern Index

Reverse index: technique -> problems that use it -> one-line essence. The real asset of this repo.

## Hash map / set — O(1) existence lookup
> Repeated "does X exist?" inside a loop -> dump data into a set/dict first.

- [0001 Two Sum](0001-two-sum/) — dict `{value: index}`; check BEFORE insert to avoid self-pairing
- [3718 Smallest Missing Multiple](3718-smallest-missing-multiple-of-k/) — set for pure existence (no index needed)
- [0013 Roman to Integer](0013-roman-to-integer/) — dict as symbol->value lookup table
- [0771 Jewels and Stones](0771-jewels-and-stones/) — purest form: build set, count membership (`sum(x in s for ...)`)

## One-way cursor / spec-following
> The problem statement IS the algorithm — a pointer walks left-to-right through stations. Win by not missing clauses.

- [0008 String to Integer (atoi)](0008-string-to-integer-atoi/) — skip spaces -> one sign -> digits -> clamp
- [0065 Valid Number](0065-valid-number/) — boolean flags variant: `seen_digit/dot/exp`, reset digit-debt after `e`

## Look-ahead / look-behind
> Decide the current element's fate by peeking at its neighbor.

- [0013 Roman to Integer](0013-roman-to-integer/) — current < next -> subtract (look-ahead)
- [0065 Valid Number](0065-valid-number/) — sign legal only after `e/E` (look-behind)

## Two pointers
> Two fingers on sorted data; advance the one pointing at the smaller item.

- [0004 Median of Two Sorted Arrays](0004-median-of-two-sorted-arrays/) — merge two sorted arrays (heart of merge sort)
- 0021 Merge Two Sorted Lists — same merge on linked lists (TODO: self-solve)

## Expand around center (two-pointer variant)
> Pointers spread APART from a point while a condition holds. Every palindrome has a center; try 2n-1 centers: `(i,i)` odd + `(i,i+1)` even.

- [0005 Longest Palindromic Substring](0005-longest-palindromic-substring/) — expand from each center, undo the one-step overshoot
- 0647 Palindromic Substrings — same expand, just count (TODO)

## Sliding window
> Two pointers on ONE sequence hugging a stretch; right extends, left jumps forward on violation; a lookup structure describes what's inside the window.

- [0003 Longest Substring Without Repeating](0003-longest-substring-without-repeating/) — dict `{char: last index}`, guard `>= left` against stale entries
- 0121 Best Time to Buy and Sell Stock — simplest relative (TODO: self-solve)

## Linked list
> Nodes = `{val, next}`; traverse with `while node: node = node.next`. Dummy head kills the first-node special case.

- [0002 Add Two Numbers](0002-add-two-numbers/) — traversal + carry + dummy head
- 0206 Reverse Linked List — pointer flipping (TODO: self-solve)

## Design: source of truth + lazy index
> When a structure can't update in place (heap), keep a dict as truth and discard stale entries on read.

- [2034 Stock Price Fluctuation](2034-stock-price-fluctuation/) — dict + two heaps, lazy deletion

## Number building / clamping
> `result = result * 10 + digit` builds numbers digit-by-digit; compute freely then clamp to `[INT_MIN, INT_MAX]`.

- [0008 atoi](0008-string-to-integer-atoi/), [0002 Add Two Numbers](0002-add-two-numbers/) (carry = grade-school addition)

## Not yet studied (deliberately)
- Binary search partition (the real O(log) median) — after the binary-search ladder step
- Sliding window, stack, sorting internals
