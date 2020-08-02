class Solution {
    public boolean detectCapitalUse(String word) {
        // judge 1st words
        if (word.length() == 1) return true;

        String subStr = word.substring(1);
        // judge 2nd words
        if (Character.isUpperCase(word.charAt(0)) && Character.isUpperCase(word.charAt(1))) {
            // judge whether all characters is upper case from 2nd to end
            return subStr.equals(subStr.toUpperCase());
        } else {
            // judge whether all characters is lower case from 2nd to end
            return subStr.equals(subStr.toLowerCase());
        }
    }
}