class Solution {
    public int titleToNumber(String s) {
        int res = 0;
        int length = s.length();
        for (int i = 0; i < length; i++) {
            res += (Math.pow(26, i) * (s.charAt(length - i -1) - 'A' + 1));
        }
        return res;
    }
}