from typing import List


class Solution:
    def twoSum(self,
               nums: List[int],
               target: int) -> List[int]:
        for a in range(len(nums)):
            for b in range(a + 1, len(nums)):
                if nums[a] + nums[b] == target:
                    return [a, b]

        return []

input1 = Solution()
print(input1.twoSum([3, 5, 1, 4, -8], 5))
