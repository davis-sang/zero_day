from typing import List


class Solution:

    def two_sum(self, num: List[int], target: int) -> List[int]:

        h = {}

        for i in range(len(num)):
            h[num[i]] = i

        for i in range(len(num)):
            y = target - num[i]

            if y in h and h[y] != i:
                return [ i, h[y]]
            
test = Solution()
test_data = [3, 2, 2, 3]

print(test.two_sum(test_data, 6))
# [0, 3]