

from typing import List
from collections import defaultdict

class Solution:
    def anagram_checker(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = defaultdict(list)
        for s in strs: # n
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            
            key = tuple(count)
            anagrams_dict[key].append(s)

        return anagrams_dict.values()
    
    # Time: O(n * m) Space: (n 


test  = Solution()
test_data = ["tan", "nat", "eat", "ate", "bat"]

t = test.anagram_checker(test_data)

print(t)
# ([['tan', 'nat'], ['eat', 'ate'], ['bat']]) -> grouped anagram

