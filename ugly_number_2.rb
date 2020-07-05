def nth_ugly_number(n)
    currIdx2 = 0
    currIdx3 = 0
    currIdx5 = 0

    nums = [1]

    (n-1).times do
        next2 = nums[currIdx2] * 2
        next3 = nums[currIdx3] * 3
        next5 = nums[currIdx5] * 5
        min = [next2, next3, next5].min
        nums.push min
        if min == next2
            currIdx2 = currIdx2 + 1 
        end

        if min == next3
            currIdx3 = currIdx3 + 1 
        end

        if min == next5
            currIdx5 = currIdx5 + 1 
        end
    end

    return nums[-1]
end
