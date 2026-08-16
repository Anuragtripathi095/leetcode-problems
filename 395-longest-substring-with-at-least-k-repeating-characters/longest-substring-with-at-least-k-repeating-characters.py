class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0

        for start in range(n):
            count = {}

            for end in range(start, n):
                count[s[end]] = count.get(s[end], 0) + 1

                valid = True

                for freq in count.values():
                    if freq < k:
                        valid = False
                        break

                if valid:
                    ans = max(ans, end - start + 1)

        return ans