  # @param {String} s
  # @return {String}
def frequency_sort(s)
  s.split(//).group_by { |e| e }.sort_by { |e, v| -v.size }.map(&:last).map(&:join).join
end
