# Filter function
# filter(func, iterable)
# filter = (item for item in iterable if function(item))
# or if func is None, check if all items are True
# filter = (item for item in iterable if item)


# Subrange

import random

v = []
for x in range(10):
    v.append(random.randrange(100))
print(f'{v=}')

def lower(value):
    if value < 50:
        return True
    return False

f = filter(lower, v)
print(f'Less than 50: {list(f)=}')



# Filter types

class Animal:
    def __init__(self, name):
        self.name = name

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

animals = []
for x in range(10):
    name = f'Animal {x}'
    if (x%2) == 0:
        animals.append(Cat(name))
    else:
        animals.append(Dog(name))

print(f'{animals=}')

for a in animals:
    print(f'Animal: {a.name}')

def cats(animal: Animal):
    return isinstance(animal, Cat)
def dogs(animal: Animal):
    return isinstance(animal, Dog)

for c in list(filter(cats, animals)):
    print(f'Cat: {c.name}')
for d in list(filter(dogs, animals)):
    print(f'Dog: {d.name}')