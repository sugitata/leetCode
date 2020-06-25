def find_duplicate(nums)
  nums.group_by{ |e| e }.select{ |k, v| v.size > 1 }.keys[0]
end