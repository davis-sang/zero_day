from typing import List

class Solution:
    def productExceptSelf(self, num: List[int]) -> List[int]:
        l_mult = 1
        r_mult = 1

        n = len(num)
        l_arr = [0] * n
        r_arr = [0] * n

        for i in range(n):
            j = -i -1
            l_arr[i] = l_mult
            r_arr[j] = r_mult
                # l_mult: 1
                # r_mult: 1
                # l_arr: [1, 0, 0, 0]
                # r_arr: [0, 0, 0, 1]
                # l_mult: 1
                # r_mult: 4
                # l_arr: [1, 1, 0, 0]
                # r_arr: [0, 0, 4, 1]
                # l_mult: 2
                # r_mult: 12
                # l_arr: [1, 1, 2, 0]
                # r_arr: [0, 12, 4, 1]
                # l_mult: 6
                # r_mult: 24
                # l_arr: [1, 1, 2, 6]
                # r_arr: [24, 12, 4, 1]
                # [24, 12, 8, 6] 
            l_mult *= num[i]
            r_mult *= num[j]
    
        return [l * r for l, r in zip(l_arr, r_arr)]
    

test = Solution()
test_data = [1,2,3,4]

print(test.productExceptSelf(test_data))

# [24, 12, 8, 6]
