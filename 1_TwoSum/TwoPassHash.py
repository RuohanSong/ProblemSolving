# Two-pass Hash Table solution for Two Sum
# time complexity: O(n)
# space complexity: O(n)

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)):
            hashmap[nums[i]] = i
            print("i=", i)
            print("nums[i]=", nums[i])
            print("hashmap[i]=", hashmap[nums[i]])
            print("hashmap:", hashmap)
            print("-------------")

        for i in range(len(nums)):
            complement = target - nums[i]
            # the first condition checks if the complement exists
            # the second condition checks if the same item is used twice
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]

        # if there is no complement, return an empty list
        return []


input1 = Solution()
print(input1.twoSum([3, 5, 1, 4, -8], -7))


