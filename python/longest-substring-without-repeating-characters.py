class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_count = dict()
        left, right = 0, 0
        n = len(s)

        result = 0

        while right < n:
            char_count[s[right]] = char_count.get(s[right], 0) + 1

            while char_count[s[right]] > 1:
                char_count[s[left]] = char_count[s[left]] - 1 
                left += 1

            right += 1
            result = max(result, right - left)

        return result
