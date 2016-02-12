# [Double Gold Star] Memoization is a way to make code run faster by saving
# previously computed results.  Instead of needing to recompute the value of an
# expression, a memoized computation first looks for the value in a cache of
# pre-computed values.

# Define a procedure, cached_execution(cache, proc, proc_input), that takes in
# three inputs: a cache, which is a Dictionary that maps inputs to proc to
# their previously computed values, a procedure, proc, which can be called by
# just writing proc(proc_input), and proc_input which is the input to proc.
# Your procedure should return the value of the proc with input proc_input,
# but should only evaluate it if it has not been previously called.

import time

def time_execution(function, inputs):
    start = time.clock()
    result = function(*inputs)
    run_time = time.clock() - start
    return result, run_time

def cached_execution(cache, proc, proc_input):
    if proc_input not in cache:
        cache[proc_input] = proc(proc_input)
    return cache[proc_input]

# Here is an example showing the desired behavior of cached_execution:

def factorial(n):
    print "Running factorial"
    result = 1
    for i in range(2, n + 1):
        result = result * i
    return result

cache = {} # start cache as an empty dictionary
### first execution (should print out Running factorial and the result)
print time_execution(cached_execution,(cache, factorial, 50))

print "Second time:"
### second execution (should only print out the result)
print time_execution(cached_execution,(cache, factorial, 50))