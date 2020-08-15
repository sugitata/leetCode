class Solution {
    public int longestPalindrome(String s) {
        int[] count = new int[Math.abs('A'-'z')+1];
        int res = 0;
        for (int i = 0; i < s.length() ;i++) count[s.charAt(i) - 'A']++;
        for (int n : count) res += n/2;
        return Math.min(res*2+1, s.length());
    }
}