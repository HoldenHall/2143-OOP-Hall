"""
Name: Holden Hall
Email: hahall0715@my.mwsu.edu
Assignment: Homework 1 - Lists and Dictionaries
Due: 19 Sep @ 1:00 p.m.
"""
#A
# Prints: 1 3
# Prints:  NameError ("Print" needs to be "print")
# Prints: 5
# Prints: True
# Prints: [1, [5, 1], 4, 2, 3]

#B 
def remove_all(el, lst):
    for i in lst:
        lst.remove(el)
#C
def add_this_many(x, y, lst):
    sum = 0
    for i in range(len(lst)):
        if lst[i] == x:
            sum+=1
    for i in range(sum):
        lst.append(y)
#D
# Prints: [3, 1, 4, 2]
# Prints: [3, 1, 4, 2, 5, 3]
# Prints: [1, 2, 3]
# Prints: [3, 1, 4, 2, 5, 3]
# Prints: []
# Prints: [1, 4, 2]
# Prints: [3, 5, 2, 4, 1, 3]

#E
def reverse(lst):
    print(lst[::-1])

#F
def rotate(lst, k):
    print(l[-k:] + l[:-k])

#H
# Prints: 3
# Prints: {'peyton manning': 1, 'tom brady': 3, 'joe flacco': 0, 'joe montana': 4}
# Prints:{'peyton manning': 1, 'tom brady': 3, 'joe flacco': 1, 'joe montana': 4}
#Prints: False
#Prints: 4
#Prints: False
#Prints: {('eli manning', 'giants'): 2, 'peyton manning': 1, 'joe montana': 4, 'tom brady': 3, 'joe flacco': 1}
#Prints: {3: 'cat', 'joe montana': 4, 'tom brady': 3, ('eli manning', 'giants'): 2, 'joe flacco': 1, 'peyton manning': 1}
#Prints: {3: 'cat', 'joe montana': 4, 'tom brady': 3, ('eli manning', 'giants'): 5, 'joe flacco': 1, 'peyton manning': 1}
#Prints: TypeError: unhashable type: 'list'

#I 
def replace_all(d, x, y):
    for key in d.keys():
        if type(d[key]) == dict:
            replace_all(d[key], x, y)
        else:
            d[key] = y if d[key] == x else d[key]
#had to google for recursion syntax "if type(d[key]) == dict:replace_all(d[key], x, y)"

#J
def rm(d, x):
    for k, v in list(d.items()):
        if v == x:
            del d[k]
