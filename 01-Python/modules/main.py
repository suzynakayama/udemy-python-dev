import random

# print(random)
#
# help(random)
#
# print(dir(random))

my_list = [1, 2, 3, 4, 5]
print(random.random())
print(random.randint(1, 10))
print(random.choice([1, 2, 3, 4, 5]))
random.shuffle(my_list)
print(my_list)

import sys

# print(sys)

first = sys.argv[1]       # when we want to access through terminal passing arguments, this will get the first argument

