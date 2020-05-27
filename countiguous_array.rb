# @param {Integer[]} nums
# @return {Integer}
def find_max_length(nums)
    arr = Array.new(2*nums.length+1, -2)
    maxLength = 0
    count = 0
    arr[nums.length] = -1
    nums.each_with_index do |n, i|
        count = count + (n == 1 ? 1 : -1)
        if arr[count + nums.length] >= -1
            maxLength = [maxLength, i - arr[count + nums.length]].max
        else
            arr[count + nums.length] = i
        end
    end
    return maxLength
end
