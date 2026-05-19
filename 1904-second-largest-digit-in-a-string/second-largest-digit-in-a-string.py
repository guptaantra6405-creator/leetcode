class Solution:
    def secondHighest(self, s: str) -> int:
        largest = -1
        sec_lar = -1

        for ch in s:
            if ch.isdigit():
                d = int(ch)
                if d>largest:
                    sec_lar = largest
                    largest = d
                elif largest>d>sec_lar:
                    sec_lar = d

        return sec_lar