# time complexity: O(log(n))
# space complexity: O(1)

from typing import List

# find upper bound

# find lower bound (only changed this if condition part):
#       if nums[mid] >= target:
#           right = mid
#       else:
#           left = mid + 1

# looking for inserting position of the target
# better solution for arrays that contain duplicate elements
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) // 2
            # still keep searching the right elements when middle is equal to target
            # because of upper bound rules:
            # insert 9 to the right of all existing 9s in the array
            if nums[mid] <= target:
                left = mid + 1
            elif nums[mid] > target:
                # if middle is larger than target
                # its index "mid" could be the inserting position of target
                right = mid
        if left > 0 and nums[left - 1] == target:
            return left - 1
        else:
            return -1


# print(Solution().search([-7,-4,3,9,9,9,12], 9))
print(Solution().search([-1,0,3,5,9,12], 9))

