# One-pass Hash Table solution for Two Sum
# time complexity: O(n)
# space complexity: O(n)

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            print(hashmap)
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            # it is important to add the new item into the hashmap after checking for its complement
            # if the new item was added already before checking, the complement could be itself!
            # in case "1 = 2 - 1"
            hashmap[nums[i]] = i

        return []


input1 = Solution()
print(input1.twoSum([3, 3], 6))


