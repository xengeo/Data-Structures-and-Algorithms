# What is good code?
# Code that is readable & scalable

# FINDING NEMO:

import time

nemo = ['nemo']
everyone = ['dory', 'dory', 'dory', 'dory', 'dory', 'dory',
            'dory', 'dory', 'dory', 'dory', 'dory', 'dory', 'nemo']


def find_nemo(array):
    now = time.time()
    for name in array:
        if name == 'nemo':
            print('FOUND NEMO')
            break
    then = time.time()
    print("Code duration: %.8f seconds" % (then - now))


find_nemo(nemo)
find_nemo(everyone)


# When we increase the size of the input to our code,
# how much does that code/algorithm slow down == BIG O
# In terms of how many OPERATIONS

# O(n) - LINEAR TIME
# O(1) - CONSTANT TIME


# BIG O RULES

# Rule 1 - Worst Case
# Rule 2 - Remove Constants
# Rule 3 - Drop non-dominants
