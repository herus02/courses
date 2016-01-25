# Define a procedure, find_second, that takes
# two strings as its inputs: a search string
# and a target string. It should return a
# number that is the position of the second
# occurrence of the target string in the
# search string.

string = "De l'audace, encore de l'audace, toujours de l'audace"
target = "audace"

def find_second(string, target) :
  return string.find(target, string.find(target) + 1)
    
print find_second(string, target)

#>>> 25

#twister = "she sells seashells by the seashore"
#print find_second(twister,'she')
#>>> 13