# @param {Integer} num_courses
# @param {Integer[][]} prerequisites
# @return {Boolean}
def can_finish(num_courses, prerequisites)
    @graph = {}
    (0..num_courses-1).each{|e| @graph[e] = []}
    prerequisites.each do |p|
        p.each_with_index do |e, i|
            if !p[i+1].nil?
                @graph[e].push p[i+1]
            end
        end
    end
    p @graph
    @order = []
    @seen = Array.new(num_courses, false)
    (0..num_courses-1).each do |v|
        if !@seen[v]
            return false if !rec(v)
        end
    end
    return true
end

def rec(v)
    @seen[v] = true
    if @graph[v].length != 0
        @graph[v].each do |nxt|
            if !@seen[nxt]
                return false if !rec(nxt)
            elsif !@order.include?(nxt)
                return false
            end
        end
    end
    @order.unshift(v)
    return true
end
