t = (1,2,3,4)
for x in t:
    print(x)

# lists, tuples, dictionaries and sets

people = ['Bryan', 'Tammy', 'Rango']
i = iter(people)
print(i)
print(next(i))
print(next(i))
print(next(i))
# print(next(i)) # throws an error because there is no more values

# Iterable class

import random
class Lotto:
    def __init__(self):
        self._max = 5
    # __iter__ = transfors a call in an iterable object
    def __iter__(self):
        # yield = returns the value, but keeps the function
        # state in memory, so, when called again, the function
        # doesn't start from beginning, starts from where 
        # yield was called
        for _ in range(self._max):
            yield random.randrange(0, 100)
    
    def set_max(self, value):
        self._max = value

print('~'*20)
lotto = Lotto()
lotto.set_max(20)

# we can loop lotto because it has "__iter__" function
for x in lotto:
    print(f'{x=}')
    

    

    
        
    