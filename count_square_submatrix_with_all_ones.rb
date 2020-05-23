# @param {Integer[][]} matrix
# @return {Integer}
def count_squares(matrix)
    height = matrix.length
    width = matrix[0].length
    if height == 0 || width == 0
        return 0
    end
    count = 0
    (0..height-1).each do |h|
        (0..width-1).each do |w|
            if matrix[h][w] == 1 && h > 0 && w > 0
                matrix[h][w] = [matrix[h-1][w], matrix[h][w-1], matrix[h-1][w-1]].min + 1
            end
            count = count + matrix[h][w]
        end
    end
    return count
end
