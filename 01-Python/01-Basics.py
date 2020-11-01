# Numbers

print(2 + 4)
print(2 - 4)
print(2 * 4)
print(2 / 4)

print(type(2 + 4))    # <class int>
print(type(2 / 4))    # <class float>

print(2 ** 3)   # 8
print(5 // 4)   # 1             - floor division, no decimals and returns an int
print(6 % 4)    # 2             - modulus operator, return the reminder

print(round(3.1))   # 3         - rounds the number
print(abs(-5))      # 5         - returns absolute value (no negative number)
print(bin(5))       # 0b101         - you get the binary representation after the b
print(int('0b101', 2))  # 5     - convert from binary to base 2 number

# Other basic functions
pow(5, 2)           # 25        - same as 5 ** 2
round(4.5678, 2)    # 4.56      - round to the nth digit
hex(512)            # '0x200'   - hexadecimal format    

# Operator precedence
# ()
# **
# * and /
# + and -

# Strings

# to print multiline strings use the triple quotes
long = '''
 O O
  u
 ___ 
'''

print(long)

# Formatted Strings

name = 'Suzy'
age = 35

print(f'My name is {name}, and I am {age} years old.')

# other way
print('My name is {}, and I am {} years old.'.format(name, age))
print('My name is {1}, and I am {0} years old.'.format(age, name))

# String Slicing

# [start:stop:stepover]

nums = '01234567'

nums[:]         # 01234567
nums[0:]        # 01234567
nums[:5]        # 01234
nums[::1]       # 01234567
nums[-1]        # 7
nums[::-1]      # 76543210   ## this will revert the string
nums[::-2]      # 7531

# Strings Functions and Methods

quote = 'To be or not to be.'

len(quote)              # length
quote.upper()           # capitalize the whole string
quote.capitalize()      # capitalize the 1st letter of the string
quote.lower()           # lowercase the string
quote.find('be')        # 3     => returns the index of the first appearance
quote.replace('be', 'me')       # replace all 'be' for 'me', but doesn't change the original string


# Boolean (bool) - in Python, booleans are capitalized

name = 'Suzy'
is_cool = True

name2 = 'Bobo'
is_cool = False

# True = 1
# False = 0

# List

my_list = ['ok', 'hey', 'hello']

new_list = my_list[:]       # creates a copy of my list

# List Functions and Methods

basket = [1,2,3,4,5]

basket.append(6)        # [1,2,3,4,5,6] - add 6 to the end of the list. It changes the list in place
basket.insert(4, 100)   # [1,2,3,4,100,5,6] - adds 100 to the index 4. It changes the list in place
basket.extend([200,201])    # [1,2,3,4,100,5,6,200,201] - concatenate the lists
basket.pop()        # [1,2,3,4,100,5,6,200] - removes the last item => ## returns the removed item
basket.pop(0)       # [2,3,4,100,5,6,200] - removes the item on the index 0
basket.remove(4)    # [2,3,100,5,6,200] - removes the value that we gave, in this case 4
basket.clear()      # [] - clear the list

basket = ['a','b','c','d']

basket.index('c')       # 2 - finds the index of c
basket.index('b', 0, 2)     # 1 - finds the index of b within the indexes 0 and 2
print('d' in basket)       # True - the letter 'd' is in basket
basket.count('d')       # 1 - counts how many 'd's the list has
basket.sort()           ## will sort the list in place
sorted(basket)          ## will sort the list in a new copy, not in place
basket.copy()           # makes a copy of the list
basket.reverse()        # reverse the list in place

list(range(1,10))            # creates a list from 1 to 9

#! Join String Method
sentence = '!'
new_sentence = sentence.join(['hi','my','name','is','Jojo'])
print(new_sentence)     # hi!my!name!is!Jojo

sentence = ' '
new_sentence = sentence.join(['hi','my','name','is','Jojo'])
print(new_sentence)     # hi my name is Jojo

## List Unpacking (destructuring)

a,b,c, *other, d = [1,2,3,4,5,6,7,8,9]

print(a)        # 1
print(b)        # 2
print(c)        # 3
print(other)    # [4,5,6,7,8]
print(d)        # 9

#  Dictionary Methods

my_dict = {
    'a': 1,
    'b': 2,
    'c': [1,2,3]
}

my_dict['d']        # returns a Keyerror
my_dict.get('d')    # returns None, does not gives an error
my_dict.get('d', 10)        # returns 10, because we set that as the default value

other_dict = dict(name='John')
print(other_dict)       # {'name': 'John'}

print('b' in my_dict)       # True
print(2 in my_dict.keys())       # False
print(my_dict.items())          # returns a tuple for each item in my_dict
my_dict.clear()         # empty the dict
third_dict = other_dict.copy()      # copies it

user = {
    'greet': 'hello',
    'name': 'Suzy',
    'age': 34,
    'nums': [1,2,3]
}

user.pop('greet')       # removes the key-value pair
user.popitem()          # removes a key-value pair and returns it
user.update({'age': 35})    # update/add the key-value pair

# Tuples

tup1 = (1,2,3,4,5,5)

tup2 = tup1[1:2]        # (2,)

x,y,z = (2,3,4)

# Tuple Methods

tup1.count(5)       # 2 - counts how many 5's the tup1 has
tup1.index(5)       # 4 - return the index of the first 5 it finds

len(tup1)           # 6

# Sets

my_set = {1,2,3,4,5,5}

print(1 in my_set)      # True
len(my_set)             # 5
new_set = my_set.copy()     # copies my set into a new set for the variable new_set

# Sets Methods

set1 = {1,2,3,4,5,}
set2 = {4,5,6,7,8,9,10}

set1.difference(set2)       # {1,2,3} - finds the difference between the first set and the second one

set1.discard(5)             # takes 5 out of set1. Returns None, but if you print set1, it will be {1,2,3,4}

set1.difference_update(set2)    # {1,2,3} - removes the items that are in both sets from the first set. It changes in place. Returns None.

set1.intersection(set2)         # {4,5} - returns what both sets contain
print(set1 & set2)              # same as intersection

set1.isdisjoint(set2)           # False - do these two sets have nothing in commom

set3 = {4, 5}

set3.issubset(set2)         # True - set 3 is a subset of set2

set3.issuperset(set2)       # False, it's the other ways around! set2 issuperset of set3.

set1.union(set2)               # {1,2,3,4,5,6,7,8,9,10}
print(set1 | set2)              # same as union








