class Solution {
    public boolean exist(char[][] board, String word) {
        boolean result = false;
        for(int i = 0; i < board[0].length; i++) {
            for(int j = 0; j < board[0].length; j++) {
                if(dfs(board, word, i, j, 0)) {
                    result = true;
                }
            }
        }

        return result;
    }

    public boolean dfs(char[][] board, String word, int i, int j, int k) {
        if(i<0 || j<0 || i>= board.length || j>= board[0].length) {
            return false;
        }

        if(board[i][j] == word.charAt(k)) {
            char curr = board[i][j];
            board[i][j] = '#';

            if(k == word.length() - 1) {
                return true;
            }else if(dfs(board, word, i-1, j, k+1)
                    || dfs(board, word, i+1, j, k+1)
                    || dfs(board, word, i, j-1, k+1)
                    || dfs(board, word, i, j+1, k+1)
                    ) {
                return true;
            }
            board[i][j]=curr;
        }

        return false;
    }
}
