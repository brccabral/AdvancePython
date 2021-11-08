# pickle can save objects instanciated 
# from built-in or upper classes, 
# from subclasses may have difficulties

import pickle

# create a decorator
def outline(func):
    def inner(*args, **kwargs):
        print('~'*20)
        print(f'Function: {func.__name__}')
        func(*args, **kwargs)
        print('-'*20)
    return inner

# create simple class
class Cat:
    def __init__(self, name, age, info):
        self._name = name
        self._age = age
        self._info = info
    
    @outline
    def display(self, msg=''):
        print(msg)
        print(f'{self._name} is a {self._age} years old cat')
        for key, value in self._info.items():
            print(f'{key=} {value=}')

othello = Cat('Othello', 15, dict(color='Black', weight=15, loves='eating'))
othello.display('Testing')


# Serialize
# put in a string
sc = pickle.dumps(othello)
print(sc) # b'\x80\x04\x95o\x00\x00\x00\x00\x00\x00\x00\x8c\x08__main__\x94\x8c\x03Cat\x94\x93\x94)\x81\x94}\x94(\x8c\x05_name\x94\x8c\x07Othello\x94\x8c\x04_age\x94K\x0f\x8c\x05_info\x94}\x94(\x8c\x05color\x94\x8c\x05Black\x94\x8c\x06weight\x94K\x0f\x8c\x05loves\x94\x8c\x06eating\x94uub.'
# put in a file
with open('cat.txt', 'wb') as f:
    pickle.dump(othello, f)

# Deserialize
# from string
my_cat = pickle.loads(sc)
print('from string')
my_cat.display('from string')
# from file
with open('cat.txt', 'rb') as f:
    disk_cat = pickle.load(f)
disk_cat.display('from disk')

# they have different memory address, 
# they are different objects even if
# they have the same data
print(my_cat) # <__main__.Cat object at 0x7f71f6611640>
print(disk_cat) # <__main__.Cat object at 0x7f71f665cca0>