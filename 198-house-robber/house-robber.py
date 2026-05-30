class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1 = 0  # dp[i-1]
        prev2 = 0  # dp[i-2]

        for money in nums:
            curr = max(prev1, prev2 + money)
            prev2 = prev1
            prev1 = curr

        return prev1