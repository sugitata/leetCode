# @param {Integer[][]} points
# @param {Integer} k
# @return {Integer[][]}
def k_closest(points, k)
    points.map{ |e| [e, Math.sqrt((e[0]*e[0])+(e[1]*e[1]))] }.sort_by{ |e| e[1] }.slice(0..k-1).map{ |e| e[0] }
end
