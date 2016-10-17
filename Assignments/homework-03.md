1) What does Python print for each of the following:

```python 
johns_bag = Bag()
johns_bag.print_bag()
# []            
            
for color in [’blue’, ’red’, ’green’, ’red’]:
    johns_bag.add_skittle(Skittle(color))
johns_bag.print_bag()
# SyntaxError: invalid character in identifier

s = johns_bag.take_skittle()
print(s.color)
# IndexError: pop from empty list

print(johns_bag.number_sold)
# 1

print(Bag.number_sold)
# 1

soumyas_bag = Bag()
soumyas_bag.print_bag()

print(johns_bag.print_bag())
# None

print(Bag.number_sold)
# 2

print(soumyas_bag.number_sold)
# 2 
```

2) Write a new method for the Bag class called take color, 
which takes a color and removes (and returns) a Skittle of that color from the bag. If there is no Skittle of that color, then it returns None.

```python 
def take_color(self, color):
        if color in self.skittles:
            temp = color
            self.skittles.remove(color)
            return temp
        else:
            return None
```
3. Write a new method for the Bag class called take all, which takes all the Skittles in the current bag
 and prints the color of the each Skittle taken from the bag.

```python 
     def take_all(self):

        for s in range(len(self.skittles)):
            self.skittles.pop()
```
