class Solution {
    public int leastInterval(char[] tasks, int n) {
        int[] freqs = new int[26];
        for (char ch : tasks) freqs[ch - 'A']++;
        int max = Integer.MIN_VALUE;
        for (int freq : freqs) max = Math.max(max, freq);
        max--;
        int spaces = max * n + max;
        for (int freq : freqs) spaces -= Math.min(freq, max);
        return spaces > 0 ? tasks.length + spaces : tasks.length;
    }
}