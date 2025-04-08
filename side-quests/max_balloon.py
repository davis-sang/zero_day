from collections import defaultdict


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter = defaultdict(int)
        balloon = "balloon"

        for c in text:
            if c in balloon:
                counter[c] += 1

        if any(c not in counter for c in balloon):
            return 0
        else:
            counter["b"] = counter["b"] // 1
            counter["a"] = counter["a"] // 1
            counter["l"] = counter["l"] // 2
            counter["o"] = counter["o"] // 2
            counter["n"] = counter["n"] // 1
            # Return the minimum value from the counter
            return min(counter.values())


# Test
s = Solution()
text = "nlaebolko"
text_1 = "loonbalxballpoon"


print("Test: ", s.maxNumberOfBalloons(text_1))
