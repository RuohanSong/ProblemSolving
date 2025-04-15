# time complexity: O(n^3)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        substring = []
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[j] not in substring:
                    substring.append(s[j])
                else:
                    break
            maxlen = max(maxlen, len(substring))
            substring.clear()
        return maxlen


print(Solution().lengthOfLongestSubstring(" "))     # 1
print(Solution().lengthOfLongestSubstring(""))      # 0
print(Solution().lengthOfLongestSubstring("abcabcbb"))# 3
print(Solution().lengthOfLongestSubstring("bbbbbbbb"))# 1
print(Solution().lengthOfLongestSubstring("12345678"))# 8
print(Solution().lengthOfLongestSubstring("pwwkew"))# 3
