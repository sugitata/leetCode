class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        int count = 0;
        if (intervals.length == 0) return count;

        // 要素[0]の小さい順でsort
        Arrays.sort(intervals, (a,b) -> (a[0]-b[0]));
        // 最も小さい要素の[1]を初期値に使用
        int currEnd = intervals[0][1];

        for (int i=1; i < intervals.length; i++) {
            // １こ前のendより先頭が小さくなってたらcount++
            if (currEnd > intervals[i][0]) {
                // どちらの要素を配列から取り除いて考えるかminでジャッジ
                currEnd = Math.min(currEnd, intervals[i][1]);
                count++;
            } else {
                currEnd = intervals[i][1];
            }
        }
        return count;
    }
}