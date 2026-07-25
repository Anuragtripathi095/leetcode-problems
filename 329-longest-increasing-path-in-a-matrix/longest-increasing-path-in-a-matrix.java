class Solution {
    private int[][] dp;
    private int[][] dirs = {{1,0},{-1,0},{0,1},{0,-1}};

    public int longestIncreasingPath(int[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;

        dp = new int[m][n];
        int ans = 0;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                ans = Math.max(ans, dfs(matrix, i, j));
            }
        }

        return ans;
    }

    private int dfs(int[][] matrix, int r, int c) {
        if (dp[r][c] != 0) {
            return dp[r][c];
        }

        int max = 1;

        for (int[] d : dirs) {
            int nr = r + d[0];
            int nc = c + d[1];

            if (nr >= 0 && nr < matrix.length &&
                nc >= 0 && nc < matrix[0].length &&
                matrix[nr][nc] > matrix[r][c]) {

                max = Math.max(max, 1 + dfs(matrix, nr, nc));
            }
        }

        dp[r][c] = max;
        return max;
    }
}