Holden Hall

1) Implement the Cat class by inheriting from the Pet class. Make sure to use superclass methods wherever possible.
In addition, add a lose_life method to the Cat class.
```python 
class Pet(object):
    def __init__(self, name, owner):
        self.is_alive = True # It’s alive!!!
        self.name = name
        self.owner = owner
    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")
    def talk(self):
        print("’...’")
        
class Cat(Pet):
    def __init__(self, name, owner, lives=9):
        Pet.__init__(self,name,owner,is_alive)
        self.lives = lives



    def talk(self):          

        print("meow!")




    def lose_life(self):
    	if self.is_alive == True:
    		self.lives - 1
    		if self.lives == 0:
    			self.is_alive = False
```
2) Assume these commands are entered in order. What would Python output?
```python
class Foo(object):
    def __init__(self, a):
        self.a = a
    def garply(self):
        return self.baz(self.a)

class Bar(Foo):
    a = 1
    def baz(self, val):
        return val

f = Foo(4)
b = Bar(3)
print(f.a)
# 4

print(b.a)
# 3

print(f.garply())
# AttributeError: 'Foo' object has no attribute 'baz'

print(b.garply())
# 3

b.a = 9
print(b.garply())
# 9

f.baz = lambda val: val * val
print(f.garply())
# 16
```
