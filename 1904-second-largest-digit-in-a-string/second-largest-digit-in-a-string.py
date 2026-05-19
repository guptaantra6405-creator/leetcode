class Solution:
    def secondHighest(self, s: str) -> int:
        digits = []

        for i in s:
            if i.isdigit():
                digits.append(int(i))

        digit_sorted = sorted(set(digits))
        if len(digit_sorted) < 2:
            return -1
        return digit_sorted[-2]