from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0

        for n in nums:
            if n-1 not in s:
                next_num = n+1
                length = 1
                while next_num in s:
                    length += 1
                    next_num += 1
                longest = max(longest, length)
        
        return longest
        # Time: O(n)
        # Space: O(n)

test = Solution()
nums = [100, 4, 200,1,3,2]
nums_1 = [0,3,7,2,5,8,4,6,0,1]
print(test.longestConsecutive(nums)) #[1,2,3,4] > 4
print(test.longestConsecutive(nums_1)) # 9



        