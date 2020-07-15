class Solution {
    public String reverseWords(String s) {
        List<String> list = Arrays.asList(s.split(" ", 0));
        Collections.reverse(list);
        String str = list.stream().filter(e -> !e.isBlank()).collect(Collectors.joining(" "));

        return str;
    }
}