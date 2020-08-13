class CombinationIterator {

    List<String> list;
    int index;
    // 組み合わせで作成するstringのlength()
    int combinationLength;
    boolean[] visited;

    public CombinationIterator(String characters, int combinationLength) {
        this.index = 0;
        this.list = new ArrayList<>();
        this.combinationLength = combinationLength;
        this.visited = new boolean[charactersG.length()];
        buildAllCombinations(characters, 0, new StringBuilder(), visited);
    }

    public void buildAllCombinations(String characters, int start, StringBuilder sb, boolean[] visited) {
        // combinationLengthに達するまでappendできたらlistに格納
        if(sb.length() == combinationLength) {
            list.add(sb.toString());
            return;
        } else {
            for(int i = start; i < characters.length(); ) {
                // 一文字ずつ訪れたかを管理する
                if(!visited[i]) {
                    sb.append(characters.charAt(i));
                    visited[i] = true;
                    buildAllCombinations(characters, i++, sb, visited);
                    visited[i-1] = false;
                    sb.setLength(sb.length() - 1);
                } else {
                    i++;
                }
            }
        }
    }

    public String next() {
        // ここでindexをインクリメントし、さらにインクリメントしたindexの内容を取得
        // listには次の組み合わせが入っている
        return list.get(index++);
    }

    public boolean hasNext() {
        // 現在のindexがlistのサイズを超えていなければnext()が存在する
        return index < list.size();

    }
}

/**
 * Your CombinationIterator object will be instantiated and called as such:
 * CombinationIterator obj = new CombinationIterator(characters, combinationLength);
 * String param_1 = obj.next();
 * boolean param_2 = obj.hasNext();
 */