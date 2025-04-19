# frequency counter

# time complexity: O(n)
# space complexity: O(n)

from collections import Counter

# some interviews may not allow to use library
# this solution is also not as extensible and flexible as the second one
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         return Counter(s) == Counter(t)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash_s = {}     # dictionary
        hash_t = {}
        for i in range(len(s)):
            # get() function gets the value of a specific key
            # create the item with value 0 if the item does not exist
            hash_s[s[i]] = hash_s.get(s[i], 0) + 1
        for j in range(len(t)):
            hash_t[t[j]] = hash_t.get(t[j], 0) + 1
        if hash_s == hash_t:
            return True
        return False


print(Solution().isAnagram("a3ag-am", "3aga-am"))