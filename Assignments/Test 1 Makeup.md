# Holden Hall

-----

## 1: Definitions: 

Using python comments, label all lines that an OOP definition could be applied to.

```python

class Employee:

   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary


emp1 = Employee("Zara", 2000)

emp2 = Employee("Manni", 5000)

emp1.displayEmployee()
emp2.displayEmployee()

print "Total Employee %d" % Employee.empCount

```
-----

```python
class Employee:   #class

   empCount = 0   #class variable

   def __init__(self, name, salary): #constructor
      self.name = name               #data member
      self.salary = salary           #data member
      Employee.empCount += 1         #attribute

   def displayCount(self):           #method
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):        #method
      print "Name : ", self.name,  ", Salary: ", self.salary


emp1 = Employee("Zara", 2000)        #Instance

emp2 = Employee("Manni", 5000)       #Instance

emp1.displayEmployee()               #object
emp2.displayEmployee()               #object

print "Total Employee %d" % Employee.empCount



```

-----

## 2: List Functions

Given the list below:

```python
States = ['Alabama','Illinois','Wyoming','New York', 'Vermont', 'New Hampshire', 'Maine', 'Texas']
```

**A)** Sort the list

**B)** Add 'Oklahoma' to the list in alphabetical order without sorting the list again. Actually, write a function that would add an item to the list in alphabetical order. Example:

```python 
States = ['Alabama','Illinois','Wyoming','New York', 'Vermont', 'New Hampshire', 'Maine', 'Texas']
States.sort()
item = input("item: ")
def addInOrder(L):
    for i in range(len(L)):
        if (L[i] > item):
            L.insert(i,item)
            break
        else:
            continue
    return L
addInOrder(States)

```




## 3: Looping over Lists
(10 Points)

Using the following list as an example: `L = [10,20,30,40,50,60,70,80,90,100]` write a function that would divide each value by its index location + 1. Our example list would turn into: `L = [10,10,10,10,10,10,10,10,10,10]`. Remember NOT to get caught up on these values. Your function should work on any list.

Usage:
```python
L =  [10,20,30,40,50,60,70,80,90,100]
NList = addPrevious(L)
print(NList)
# prints: [10,10,10,10,10,10,10,10,10,10]
```

Your answer should consist of just the function definition and none of the usage I provided above.

```python
def addPrevious(L):
    for i in range(len(L)):
        L = L[:]
        if( i < len(L)):
            L[i] = (L[i]/L[i+1])
        else:
            L[i] = (L[i]/L[0])
```
-----

## 4: Looping over Dictionaries
(10 Points)

Given the following dictionary: 
```python
months = { 1 : "January", 
     	2 : "February", 
    	3 : "March", 
        4 : "April", 
     	5 : "May", 
     	6 : "June", 
    	7 : "July",
        8 : "August",
     	9 : "September", 
    	10 : "October", 
        11 : "November",
    	12 : "December" }
```
Iterate over this dictionary, and create a new one that only uses the first three letters of the month. Also make the new months all lowercase. Your new dictionary should look like:

```
abbr_months = {1:"jan",
        2 :"feb",
        3 :"mar",
        4 : "apr", 
     	5 : "may", 
     	6 : "jun", 
    	7 : "jul",
        8 : "aug",
     	9 : "sep", 
    	10 : "oct", 
        11 : "nov",
        12 : "dec" }
```

To help you look up `string slicing` and `lower`. 

Your answer should include just the code that loops and creates the new dictionary.

```python
def newDict(D):
    abbr_months = {}
    for k,v in D.items():
        abbr_months[k] = (v.lower()[:3])
```
-----

## 5: Min and Max
(10 Points)

- Assume that pythons built in min , max , and sort functions are broken. Write a function that receives a list then traverses the list and returns the `min` , `max`, and `average` values in a tuple.

```python
def miniStats(L):
""" 
@Description: Finds the min,max,and average values in a list
@Params: L (list)
@Returns: tuple (int,int,double)
"""
	# Start with a copy of the list so we don’t modify the original.
   L = L[:]
   for i in range(len(L)):
        if( i == 0):
            self.max,self.min,self.average = L[0]
        elif(i < len(L)):
            if(L[i] < min):
                self.min = L[i]
            if(L[i] > max):
               self.max = L[i]
            average +=L[i]
        else:
            if(L[i] < min):
                self.min = L[i]
            if(L[i] > max):
                self.max = L[i]
            average +=L[i]
            average /= 2
            return (min,max,average)




```

When writing your answer, include the entire function definition (without the comment block).

-----



## 6: Prime Class


Write a class called `myPrimes` that represents a collection of your prime numbers. 
- `addPrime` : 
    - receives a prime number and adds it to your collection of primes
    - it must be checked to make sure it's prime! (should be a private method that does this).
- `removePrime`:
    - a method will remove a prime from your list
- `printPrimes`:
    - this method will print your prime numbers out 
 ```python
 import math
class myPrimes(object):

    def __init__(self):
        self.L = []
        self.check = True
        self.num = 1
    

    def __primeCheck(self, num):
        length = math.sqrt(num)
        length = int(length)
        for i in range(length+1):
            if(i == 0):
                continue
            if(i == 1):
                continue
            if((num/i).is_integer() == True):
                self.check = False
                break
    
    def addPrime(self, num):
        self.__primeCheck(num)
        if(self.check == True):
            self.L.append(num)
            self.check = False

    def removePrime(self,num):
        self.L.remove(num)

    def printPrimes(self):
        print(self.L)
```

-----
