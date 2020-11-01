# Udemy Complete Python Developer in 2021

## By Andrei Neagoie

### [Link](https://www.udemy.com/course/complete-python-developer-zero-to-mastery/)

<h3 id='summary'>Summary</h3>

- [Udemy Complete Python Developer in 2021](#udemy-complete-python-developer-in-2021)
  - [By Andrei Neagoie](#by-andrei-neagoie)
    - [Link](#link)
  - [Python](#python)
    - [Fundamental Data Types](#fundamental-data-types)
        - [Classes => Custom Types](#classes--custom-types)
        - [Specialized Data Types => Modules](#specialized-data-types--modules)
        - [None](#none)
      - [Variables](#variables)
      - [Formatted Strings](#formatted-strings)
      - [Lists](#lists)
          - [Matrix](#matrix)
      - [Dictionary](#dictionary)
      - [Tuples](#tuples)
      - [Sets](#sets)
    - [Conditional Logic](#conditional-logic)

## Python

### Fundamental Data Types

- int - integer number
- float - decimal number
- complex - complex number equivalent to a real number + an imaginary number
- bool - boolean, True or False
- str - strings, they are immutable
- list - ordered collection of items, changeable and allows duplicates
- tuple - ordered collection of items, unchangeable and allows duplicates
- set - unordered collection of items, changeable and doesn't allows duplicates
- dict - unordered key-value pairs of items, changeable and doesn't allows duplicates

##### Classes => Custom Types

##### Specialized Data Types => Modules

##### None

Absence of value, like 'null' in JS.

#### Variables

Store information that can be used later in the program. In python we define a variable directly. Ex:
`name = Suzy`

In python, variables:

- use snake_case
- should start with lowercase or underscore
- use only letters, numbers, underscores
- are case sensitive
- should not overwrite keywords

Constants should use uppercase.

'Dunder' are double underscores, and should not be used for new variables.

#### Formatted Strings
To add a variable within a string, we can use two ways:

```python
name = 'Suzy'
age = 35

print(f'My name is {name}, and I am {age} years old.')

# other way
print('My name is {}, and I am {} years old.'.format(name, age))
print('My name is {1}, and I am {0} years old.'.format(age, name))
```

#### Lists

Form of arrays. Ordered collection of items that can be changed and allows duplicate items.

###### Matrix

2D Lists

```python
matrix = [
    [0,1,0],
    [1,1,1],
    [0,1,0]
]

matrix[0][1]        # 1
```

#### Dictionary

Objects. Unordered key-value pairs of items, changeable and doesn't allows duplicates.

Dict keys needs to be immutable and unique. We can use tuples, numbers, booleans or strings.

#### Tuples

Like Lists, but immutable. Ordered collection of items, unchangeable and allows duplicates.

Slightly faster than lists.

```python
my_tuple = (1,2,3)
```

#### Sets

Unordered collection of items, changeable and doesn't allows duplicates.

```python
my_set = {1,2,3,4,5}

# if I had like this: {1,2,3,4,5,5} , the second 5 would never be added to our set
```

### Conditional Logic

```python
is_old = True
is_licensed = True

if is_old:
    print('you are old enough!')
elif is_licensed:
    print('you can drive!')
else:
    print('You are not old enough!')

age = 21

if is_old and age >= 21:
    print('yay! you can drink!')
elif is_old and age < 21:
    print('you are too young to drink! Here is some milk.')
```





