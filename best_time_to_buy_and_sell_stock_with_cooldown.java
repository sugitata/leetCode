class Solution {
    public int maxProfit(int[] prices) {
        // use dynamic programming
        if (prices == null || prices.length <= 1) {
            return 0;
        }
        int n = prices.length;
        int[][] dp = new int[n][2];
        dp[0][0] = -prices[0]; // 買った場合　買ったのでその金額マイナスになる
        dp[0][1] = 0; // 売った場合

        for (int i = 1; i < n; i++) {
            // 売った場合
            // 結果が高いか安いかの比較
            dp[i][1] = Math.max(dp[i-1][1], dp[i-1][0] + prices[i]);

            // 買った場合
            dp[i][0] = dp[i-1][0];
            if(i >= 2) {
                dp[i][0] = Math.max(dp[i][0], dp[i-2][1] - prices[i]);
            } else {
                dp[i][0] = Math.max(dp[i][0], -prices[i]);
            }
        }

        return dp[n-1][1];
    }
}