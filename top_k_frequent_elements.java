class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        List<Integer> list =
            Arrays.stream(nums).boxed().collect(Collectors.toList());
        Map<Integer, Long> map =
            list.stream()
            .collect(Collectors.groupingBy(Function.identity(), Collectors.counting()));
        Set<Integer> set = map.entrySet().stream()
            .sorted(Map.Entry.comparingByValue(Comparator.reverseOrder()))
            .limit(k)
            .collect(Collectors.toMap(
                Map.Entry::getKey, Map.Entry::getValue, (e1, e2) -> e1, LinkedHashMap::new))
            .keySet();
        int[] ans = new int[set.size()];
        int index = 0;
        for(Integer e : set) ans[index++] = e.intValue();
        // System.out.println(list);
        // System.out.println(map);
        // System.out.println(ans);
        return ans;
    }
}
