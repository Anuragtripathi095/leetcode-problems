class Solution:
    def partition(self, s: str):
        res = []

        def isPalindrome(sub):
            return sub == sub[::-1]

        def backtrack(start, path):
            if start == len(s):
                res.append(path[:])
                return

            for end in range(start, len(s)):
                substring = s[start:end+1]
                if isPalindrome(substring):
                    path.append(substring)
                    backtrack(end + 1, path)
                    path.pop()  # backtrack

        backtrack(0, [])
        return res