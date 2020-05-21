# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val = 0, left = nil, right = nil)
#         @val = val
#         @left = left
#         @right = right
#     end
# end
# @param {TreeNode} root
# @param {Integer} k
# @return {Integer}
def kth_smallest(root, k)
    @count = 0

    kth_smallest_root = return_kth_smallest(root, k)
    return kth_smallest_root.val
end

def return_kth_smallest(root, k)
    if root == nil
        return nil
    end

    left = return_kth_smallest(root.left, k)

    if left != nil
        return left
    end

    # current
    @count += 1
    if @count == k
        return root
    end

    return return_kth_smallest(root.right, k)
end