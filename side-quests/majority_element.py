class Solution:
    def majority_element(self, nums: list[int]) -> int:
        set_num = {}

        for num in nums:
            if num in set_num:
                set_num[num] += 1
            else:
                set_num[num] = 1
        max_count = 0
        result = 0
        for key, value in set_num.items():
            if value > max_count:
                max_count = value
                result = key
        return result


# Test
s = Solution()
nums = [2, 2, 1, 1, 1, 2, 2]
nums_1 = [3, 2, 1, 1, 2, 2, 2, 3, 2]
print("Test: ", s.majority_element(nums))
