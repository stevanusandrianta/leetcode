class Solution:
    def isSubsetOf(self, lookup: dict, data: dict):
        for k in lookup.keys():
            if lookup.get(k, 0) > data.get(k, 0):
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        expected_char_count = dict()
        for el in t:
            expected_char_count[el] = expected_char_count.get(el, 0) + 1

        char_count = dict()
        left, right, n = 0, 0, len(s)

        min_char_count = float("inf")
        result = ""
        
        while left < n and right < n:
            while self.isSubsetOf(expected_char_count, char_count) == False and right < n:
                char_count[s[right]] = char_count.get(s[right], 0) + 1
                right += 1
                # print(right, left, self.isSubsetOf(expected_char_count, char_count))

            if right == n and left == 0 and self.isSubsetOf(expected_char_count, char_count) == False:
                return ""

            while self.isSubsetOf(expected_char_count, char_count) == True and left < n:
                if right - left < min_char_count:
                    min_char_count = right - left
                    result = s[left:right]
                char_count[s[left]] -= 1
                left += 1
                # print(right, left, self.isSubsetOf(expected_char_count, char_count))

        return result
