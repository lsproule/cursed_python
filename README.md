# Cursed Python 1.0


I took it upon myself to fix python's problems. First thing to note,
there is **no gil**! This is using the optional compile flags that makes
the gil optional.

# Functions
second and definitely more important.

```python
def some_function():
   ... 
```

will now be

```
fnc some_function():
    ...
```

---
# Pass

of course if you don't know the implementation we could use 

```python
def some_function():
    pass 
```
or we could use the fixed syntax

```python
fnc some_function():
    idfk 
```

because we are inclusive and there are many spanish developers, there's also

```python
fnc some_function():
    niputaidea
```

---
# For 

I love rust, so I decided we can't go without there loops

so

```python
for x in range(10):
    print(x)
```

can  now be expressed as

```
loop x in range(10):
   print(x) 
```

I know  some python 2 developers are sad because they see range so...

## xrange

I brought back xrange

```python
loop x in xrange(10):
   print(x) 
```

# looping helpers

I felt bad for lua developers, so instead of

```python
xs = [1,2,3]
ys = [3,4,5]
for x,y in zip(xs,ys):
    print(x,y)
```
we can now say

```
xs = [1,2,3]
ys = [3,4,5]
loop x, y in ipairs(xs, ys):
    print(x,y)
```

---
#  Classes

you may know that classes in python can be made as such:

```python
class A:
    ...

```

well, c programmers don't like that there aren't any structs

so let's fix that

```
struct A:
    ...
```

---
# while

in python we have while loops

```python
x=0
while x !=100
    x += 1
    print(x)
```

but ruby really always had the right idea.

```
until not (x == 100):
    x+=1
    print(x)
```
---
# imports

we know how python imports work
```python
import itertools
from functools import reduce
```

we know javascript developers have never seen an import statement, so

```
require itertools
from functools require reduce
xs = [1, 3, 5, 6, 2] 
  
print(reduce(lambda a, b: a+b, xs)) 
```
---
# datatypes

## list
list in python
```python
list(range(10))
```
arr in cursed python

```
arr(range(10))
```

## dicts 

dictionary in python
```python
dict(zip(['a', 'b',  'c'],[1,2,3]))
```
objs^1 in cursed python,


```
obj(ipairs(['a', 'b',  'c'],[1,2,3]))
```
note^1 ps don't confuse objs with objects not the same thing

