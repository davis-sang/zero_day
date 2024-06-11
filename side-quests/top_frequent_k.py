import heapq
from collections import Counter
from typing import List

class Solution:
    # Time : O(n * log(k)) Space: O(n)
    def frequency_k(self, num: List[int], k: int) -> List[int]:
        counter = Counter(num)
        heap = []

        for key, val in counter.items():
            if len(heap) < k:
                heapq.heappush(heap, (val, key))
            else:
                heapq. heappushpop(heap, (val, key))

        return [h[1] for h in heap]
    # Time O(n), Space O(n)
    def top_frequent(self, num: List[int], k: int) -> List[int]:
        n = len(num)

        counter = Counter(num)
        bucket = [0]*(n + 1) # [1,2,3] => [0, 0, 0, 0]

        for num, freq in counter.items():
            if bucket[freq] == 0:
                bucket[freq] = [num]
            else:
                bucket[freq].append(num)

        ret = []
        for i in range(n, -1, -1):
            if bucket[i] != 0:
                ret.extend(bucket[i])
            if len(ret) == k:
                break
        return ret


test = Solution()
test_data = [1,1,1,2,2,3]
k = 2
# O(n * logk)
print(test.frequency_k(test_data, k))
# O(n)
print(test.top_frequent(test_data, k))


