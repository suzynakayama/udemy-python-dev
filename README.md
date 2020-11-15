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
        - [Ternary Operator (Conditional Expression)](#ternary-operator-conditional-expression)
        - [Short Circuiting using 'OR' and 'AND'](#short-circuiting-using-or-and-and)
          - ['IS' vs '=='](#is-vs-)
        - [Range and Enumerate](#range-and-enumerate)
    - [Functions](#functions)
        - [*args and **kwargs](#args-and-kwargs)
    - [Walrus Operator - Python 3.8](#walrus-operator---python-38)
    - [global and nonlocal](#global-and-nonlocal)
    - [OOP - Object Oriented Programming](#oop---object-oriented-programming)
        - [@classmethod and @staticmethod](#classmethod-and-staticmethod)
        - [The 4 Pilars of OOP](#the-4-pilars-of-oop)
        - [`super()` Method](#super-method)
          - [Introspection](#introspection)
        - [Multiple Inheritance](#multiple-inheritance)
        - [Method Resolution Order (MRO)](#method-resolution-order-mro)

## Python

### Fundamental Data Types

[Summary](#summary)

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

[Summary](#summary)

Absence of value, like 'null' in JS.

#### Variables

[Summary](#summary)

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

[Summary](#summary)

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

[Summary](#summary)

Form of arrays. Ordered collection of items that can be changed and allows duplicate items.

###### Matrix

[Summary](#summary)

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

[Summary](#summary)

Objects. Unordered key-value pairs of items, changeable and doesn't allows duplicates.

Dict keys needs to be immutable and unique. We can use tuples, numbers, booleans or strings.

#### Tuples

[Summary](#summary)

Like Lists, but immutable. Ordered collection of items, unchangeable and allows duplicates.

Slightly faster than lists.

```python
my_tuple = (1,2,3)
```

#### Sets

[Summary](#summary)

Unordered collection of items, changeable and doesn't allows duplicates.

```python
my_set = {1,2,3,4,5}

# if I had like this: {1,2,3,4,5,5} , the second 5 would never be added to our set
```

### Conditional Logic

[Summary](#summary)

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

##### Ternary Operator (Conditional Expression)

[Summary](#summary)

*condition_if_true if contition else condition_if_else*

```python
is_friend = True
can_message = "message allowed" if is_friend else "not allowed to message"
```

##### Short Circuiting using 'OR' and 'AND'

[Summary](#summary)

'OR' will return when it finds the first truthy value.
'AND' will return only if both are truthy.

```python
is_friend = True
is_user = True

if is_friend or is_user:
    print('best friends forever')
```

Some other operators are: `<, >, ==, !=, >=, <=`

'NOT' will return the opposite: if you pass True, it will return false, and vice-versa.

###### 'IS' vs '=='

[Summary](#summary)

'IS' will look for the place in memory, it will check is the place in memory is the same.
'==' will check the equality of the values.

```python
print(True == 1)                # True
print('' == 1)                  # False
print([] == 1)                  # False
print(10 == 10.0)               # True
print([] == [])                 # True

print(True is 1)                # False
print('' is 1)                  # False
print([] is 1)                  # False
print(10 is 10.0)               # False
print([] is [])                 # False
```


##### Range and Enumerate

[Summary](#summary)

The range method can be used to create a range. Note, the first parameter is the initial number, the second parameter is the final number (not inclusive), and the third parameter is the step. The step can be ascending (positive number) or descending (negative number).

The enumerate adds a counter to the iterable and returns it. Ex:
```python
x = ['a', 'b', 'c']

y = enumerate(x)
print(list(y))      # [(0,'a'), (1,'b'), (2,'c')]

z = enumerate(x,2)
print(list(z))      # [(2,'a'), (3,'b'), (4,'c')]
```

### Functions

[Summary](#summary)


Positional Arguments - when we use this type of arguments, we need to pay attention to the order that we add them.

```python
def my_function(arg_a, arg_b, arg_c):
    # do something
    pass

my_function(a, b, c)
```

Keyword Arguments - it means we are giving the name of the parameter to the argument, so we don't really need to care for the arguments order.

```python
def my_function(arg_a, arg_b, arg_c):
    # do something
    pass

my_function(arg_a=a, arg_c=c, arg_b=b)
```

Default Parameters - allow us to give what we want the parameters to default to if no argument is given to the function when called.

```python
def my_function(arg_a, arg_b=None, arg_c):
    # do something
    pass

my_function(arg_a=a, arg_c=c)
```

##### *args and **kwargs

[Summary](#summary)


*args - shows that function can accept any number of positional arguments

**kwargs - shows that function can accept any number of keyword arguments

When using both, the **kwargs always comes after the *args.

Rule of parameters/arguments:
**params, *args, default parameters, **kwargs**

### Walrus Operator - Python 3.8

[Summary](#summary)


`:=`

Way of assign values to variables as part of a longer expression.
Ex:

```python
a = 'hellooooooo'

if ((n := len(a)) > 10):
    print(f'too long {n} elements')
```

### global and nonlocal

[Summary](#summary)


In order to use a global variable inside a function we have 2 ways:

- Use the `global` keyword within the function with the variable
- Pass as argument to the function

`nonlocal` is a new keyword (python 3.8) that allows you to use the parent scope within the inner scope.

```python
def outer():
    x = 'local'
    def inner():
        nonlocal x
        x = 'nonlocal'
        print('inner: ', x)
    inner()
    print('outer: ', x)

outer()             # inner: nonlocal // outer: nonlocal

```

### OOP - Object Oriented Programming

[Summary](#summary)

Everything in python is an object. OOP is a paradigms, a way to think and structure your code.

`__init__` is a constructor magic method and it's called every time the class is instantiated.

##### @classmethod and @staticmethod

[Summary](#summary)

They are both decorators for methods that can be called on uninstatiated class objects.

`@classmethod` - first parameter is always `cls`, the class. So you can use the class itself within the method, for example creating a new instance.

`@staticmethod` - works the exact same way, but you don't have access to the class. Use a static method when you don't care about anything of the class. You will just create a regular method that doesn't have access to the `cls` of the `self`.

##### The 4 Pilars of OOP

[Summary](#summary)

- Encapsulation - binding of data and functions that manipulate that data that we encapsulate into one big object, so we keep everything in this big box that users or code or other machines can interact with. And these data and functions are what we call as attributes and methods.

- Abstraction - means hiding the information and giving only what is necessary.
  - Private Variables/Attributes - in Python there is no true private variables. What we can do is add an `_` before the variable, however it does not prevent people from changing it, it's a convention that the `_` before a variable should not be touched/changed.

- Inheritance - allows new objects (sub-classes or derived classes) to inherit from a pre-existent object.

```python
class User():
    def sign_in(self):
        print('logged in')

class Wizard(User):
    pass

wizard1 = Wizard()
print(wizard1.sign_in())
```

Note: `isinstance(instance, Class)` is a built-in function in python to figure out if the instance is an instance of the Class we are trying to figure out.

- Polymorphism - it means 'many forms'. It refers to the way that object classes can share the same method name, but those methods can act differently depending on how the method is called.
Example:

```python
for item in [circle, square]:
    print(item)

# even though I am printing item, each time the item is a different object, so I'll have 2 different outputs for the same line of code.
```

##### `super()` Method

[Summary](#summary)

When we want to call the superclass init function within the init function of a subclass, we use the `super()` method. Ex:

```python
class User():
    def __init__(self, email):
        self.email = email

class Agent(User):
    def __inti__(self, name, age, email):
        super().__init__(email)
        self.name = name
        self.age = age
```

###### Introspection

[Summary](#summary)

Figure out the type of object when the code runs.

We can use `dir(object)` and we will know all the method and attributes from the object.

##### Multiple Inheritance

[Summary](#summary)

If we want a class to inherit from more than one class, we just pass within the brackets. Ex. `class Hybrid(Wizard, Archer):`

One thing to keep in mind is that you need to __init__ the Hybrid class with both superclasses __init__ methods.

```python
class Hybrid(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)
```

##### Method Resolution Order (MRO)

[Summary](#summary)

You can use the `__mro__` or `.mro()` to figure out the order of classes (when you have multiple inheritance) the code will look for in order to find the method/attribute you are 'calling'.