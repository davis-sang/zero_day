# Time complexity demo
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str):
        # Time: O(n + m)
        # Space: O(n)
        s = set(jewels)
        count = 0

        for stone in stones:
            if stone in s:
                count += 1
            # if stone in jewels:
            #     count+=1
            # This results in complexity of O(m * n)

        return count


n = Solution()

jewel = "aA"
stone = "aAASsbfbed"

Test = n.numJewelsInStones(jewel,stone)
print("Test: ", Test) # Expect 4
