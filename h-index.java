class Solution {
    public int hIndex(int[] citations) {
        Arrays.sort(citations);
        int res = 0;
        for(int i=citations.length-1; i>=0 ; i--) {
            int curr = citations.length - i;
            if(citations[i]>=curr) {
                res = curr;
            } else {
                break;
            }
        }
        return res;
    }
}