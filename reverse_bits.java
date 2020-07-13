public class Solution {
    // you need treat n as an unsigned value
    public int reverseBits(int n) {
        int result = 0;

        for(int i = 0; i < 32; i++) {
            int currBit = (n >> i) & 1;
            result += (currBit << (32 - 1 - i));
        }
        return result;
    }
}