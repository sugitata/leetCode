# @param {Integer[]} citations
# @return {Integer}
def h_index(citations)
    citations.reverse!
    hIndex = 0
    citations.each_with_index do |c, i|
        hIndex = [hIndex, [c, i+1].min].max
    end

    hIndex
end
