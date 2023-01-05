class Solution:

    def isPalindrome(self, s: str) -> bool:
        mid = int(len(s)/2)
        for i in range(mid):
            if s[i] != s[len(s)-1-i]:
                return False
        return True

    def countSubstrings(self, s: str) -> int:
        result = 0
        n = len(s)
        mem = dict()

        for i in range(n):
            for j in range(i,n):
                substring = s[i:j+1]
                if mem.get(substring):
                    is_substring_palindrome = mem.get(substring)
                else:
                    is_substring_palindrome = self.isPalindrome(substring)
                    mem[substring] = is_substring_palindrome

                if is_substring_palindrome:
                    result += 1

        return result