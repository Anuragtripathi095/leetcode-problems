class Solution {

    public int getMoneyAmount(int n) {

        int[][] dp = new int[n + 1][n + 1];

        return solve(1, n, dp);
    }

    private int solve(int start, int end, int[][] dp) {

        // No cost if there is only one number
        if (start >= end)
            return 0;

        // Already computed
        if (dp[start][end] != 0)
            return dp[start][end];

        int ans = Integer.MAX_VALUE;

        // Try every possible first guess
        for (int i = start; i <= end; i++) {

            int left = solve(start, i - 1, dp);
            int right = solve(i + 1, end, dp);

            int cost = i + Math.max(left, right);

            ans = Math.min(ans, cost);
        }

        dp[start][end] = ans;

        return ans;
    }
}