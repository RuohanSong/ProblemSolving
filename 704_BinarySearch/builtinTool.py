# time complexity: O(log(n))
# space complexity: O(1)

import bisect
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # bisect looks for the position of inserting a new element
        # to keep an array sorted
        index = bisect.bisect_left(nums, target)
        # make sure the index is inside the bound of the array
        # so that there is no IndexError
        if index < len(nums) and nums[index] == target:
            return index
        else:
            return -1


print(Solution().search([9,9,9,12,15], 9))
print(Solution().search([-7,-4,3,9,9,9,12], 20))
print(Solution().search([-7,-4,3,9,9,9,12], -10))
print(Solution().search([-1,0,3,5,9,12], 9))