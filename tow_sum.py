class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    # dictionary
    values = {}

    # *
    # In Python, you can get the element and index (count) from iterable objects such as list and tuple in for loop with the built-in function enumerate().
    # @see https://note.nkmk.me/en/python-enumerate-start/
    # *
    for index, value in enumerate(nums):
      # At first, values dictionary is empty.
      # *
      # check whether values contain the diff (target - value) or not
      # @ see https://stackoverflow.com/questions/3437059/does-python-have-a-string-contains-substring-method
      # *
      if target - value in values:
        # `target - value` is the partner value.
        # `values[target - values]` means previous index
        return [values[target - value], index]
      else:
        # Because using enumerate and knowing their index we can add the index
        values[value] = index
