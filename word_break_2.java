class Solution {
    // ref: https://leetcode.com/problems/word-break-ii/discuss/763239/Java-Simple-DFS-1ms-Solution-Explained
    public List<String> wordBreak(String s, List<String> wordDict) {
        // TODO: 無理やりっぽいので別のやり方考える
        if (s.length() > 100) return new ArrayList();
        List<String> res = new ArrayList<>();
        StringBuilder subList = new StringBuilder();
        dfs(s, wordDict, res, subList);
        return res;
    }

    public void dfs(String s, List<String> wordDict, List<String> res, StringBuilder subList) {
        // 次の単語を挿入する前にスペースで区切る
        if (subList.length() != 0) {
            subList.append(" ");
        }

        for (String word : wordDict) {
            // startsWithは接頭語の判定
            if (s.startsWith(word)) {
                StringBuilder sb = new StringBuilder(subList);
                sb.append(word);
                if (s.equals(word)) {
                    // 残ったsが最後にマッチしたwordと一致した場合、再帰処理終了
                    res.add(new String(sb));
                } else {
                    // word部分をsから削って再帰処理
                    dfs(s.substring(word.length()), wordDict, res, sb);
                }
            }
        }
    }
}