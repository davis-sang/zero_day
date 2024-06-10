from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]):
        # O(1) using a hash
        h = set()
        for num in nums:
            if num in h:
                return True
            else:
                h.add(num)
        return h
    

test = Solution()
test_data = [1,2,3,4,4,5]
# Returns true
print(test.containsDuplicate(test_data))