# time complexity: O(n)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0

        # store the index of a character from 1 to n
        charToNextIndex = {}

        i = 0
        for j in range(n):
            # have a duplicate
            if s[j] in charToNextIndex:
                i = max(charToNextIndex[s[j]], i)

            ans = max(ans, j-i+1)
            charToNextIndex[s[j]] = j+1

        return ans


print(Solution().lengthOfLongestSubstring(" "))     # 1
print(Solution().lengthOfLongestSubstring(""))      # 0
print(Solution().lengthOfLongestSubstring("abcabcbb"))# 3
print(Solution().lengthOfLongestSubstring("bbbbbbbb"))# 1
print(Solution().lengthOfLongestSubstring("12345678"))# 8
print(Solution().lengthOfLongestSubstring("pwwkew"))# 3