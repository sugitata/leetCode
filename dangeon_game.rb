def calculate_minimum_hp(dungeon)
    n = dungeon.length
    m = dungeon[0].length

    minimumHp = Array.new(n, Array.new(m, nil))
    (n-1).downto(0) do |i|
        (m-1).downto(0) do |j|
            if i == n-1 && j == m-1
                # P点
                minimumHp[i][j] = [1, 1-dungeon[i][j]].max
            elsif i == n-1
                # 上に戻っていく
                minimumHp[i][j] = [1, minimumHp[i][j+1]-dungeon[i][j]].max
            elsif j == m-1
                # 右に戻っていく
                minimumHp[i][j] = [1, minimumHp[i+1][j]-dungeon[i][j]].max
            else
                # 上か右に戻っていく
                minimumHp[i][j] = [1, [minimumHp[i+1][j], minimumHp[i][j+1]].min - dungeon[i][j]].max
            end
        end
    end

    minimumHp[0][0]
end