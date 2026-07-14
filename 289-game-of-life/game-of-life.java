class Solution {
    public void gameOfLife(int[][] board) {

        int m = board.length;
        int n = board[0].length;

        int[][] copy = new int[m][n];

        int[] row = {-1,-1,-1,0,0,1,1,1};
        int[] col = {-1,0,1,-1,1,-1,0,1};

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {

                int live = 0;

                // Count live neighbors
                for (int k = 0; k < 8; k++) {
                    int r = i + row[k];
                    int c = j + col[k];

                    if (r >= 0 && r < m && c >= 0 && c < n && board[r][c] == 1) {
                        live++;
                    }
                }

                // Apply rules
                if (board[i][j] == 1) {
                    if (live < 2 || live > 3)
                        copy[i][j] = 0;
                    else
                        copy[i][j] = 1;
                } else {
                    if (live == 3)
                        copy[i][j] = 1;
                    else
                        copy[i][j] = 0;
                }
            }
        }

        // Copy result back
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                board[i][j] = copy[i][j];
            }
        }
    }
}