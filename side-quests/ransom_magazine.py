class Solution:
    def can_construct(self, ransom_note: str, magazine: str) -> bool:
        count = {}

        for c in magazine:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1
        for c in ransom_note:
            if c in count:
                if count[c] == 1:
                    del count[c]
                else:
                    count[c] -= 1
            else:
                return False
        return True


s = Solution()
ransom_note = "aa"
magazine = "aab"

Test = s.can_construct(ransom_note, magazine)
print("Test: ", Test)
