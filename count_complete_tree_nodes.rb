def count_nodes(root)
    @count = 0
    helper(root) unless root.nil?
    @count
end

def helper(curr)
    @count = @count + 1

    if curr.left.nil? == false
        helper(curr.left)
    end

    if curr.right.nil? == false
        helper(curr.right)
    end
end
