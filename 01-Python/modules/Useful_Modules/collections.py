from collections import Counter, defaultdict, OrderedDict

li = [1, 2, 3, 4, 5, 6, 7]

print(Counter(li))

sentence = 'hello, python is awesome!'

print(Counter(sentence))

dictionary = defaultdict(lambda: 'Does not exist.', {'a': 1, 'b': 2})

print(dictionary['b'])
print(dictionary['c'])


# you don't need to use OrderedDict on newer python versions, since that is the default now
d1 = OrderedDict()
d1['a'] = 1
d1['b'] = 2

d2 = OrderedDict()
d2['a'] = 2
d2['b'] = 1

print(d2 == d1)
