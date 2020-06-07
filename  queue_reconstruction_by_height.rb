# @param {Integer[][]} people
# @return {Integer[][]}
def reconstruct_queue(people)
    numOfPeople = people.length
    @people = people
    @newQueue = Array.new(numOfPeople, nil)
    numOfPeople.times { helper() }

    @newQueue
end

def helper
    shortest = @people.min {|a, b| a[0] <=> b[0]}

    shortests = @people.select { |p| p[0] == shortest[0] }
    if shortests.length > 1
        shortest = shortests.max {|a, b| a[1] <=> b[1]}
    end

    k = shortest[1]
    newIndex = @newQueue.map.with_index{|e, i| [e, i]}.select{|e| e[0].nil?}[k][1]
    @newQueue[newIndex] = shortest

    @people.delete(shortest)
end
