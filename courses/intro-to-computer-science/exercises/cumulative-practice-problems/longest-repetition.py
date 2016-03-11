# Question 8: Longest Repetition

# Define a procedure, longest_repetition, that takes as input a
# list, and returns the element in the list that has the most
# consecutive repetitions. If there are multiple elements that
# have the same number of longest repetitions, the result should
# be the one that appears first. If the input list is empty,
# it should return None.

def longest_repetition(list):
  if not list:
    return None

  end = len(list) - 1
  biggest = [list[0], 0]
  count = 0
  for i in range(0, end):
    if list[i] == list[i + 1]:
      count += 1
      if count > biggest[1]:
        biggest[0] = list[i + 1]
        biggest[1] = count
      continue
    else:
      if list[i] != list[i + 1]:
        count = 0
  return biggest[0]

#For example,

print longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1])
# 3

print longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd'])
# b

print longest_repetition([1,2,3,4,5])
# 1

print longest_repetition([])
# None

print longest_repetition([2, 2, 3, 3, 3])
# 3

