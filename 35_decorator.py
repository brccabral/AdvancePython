# wrong way
def test_decorator(func):
    print('before')
    func()
    print('after')

@test_decorator
def do_stuff():
    print('Doing stuff')

# running above code will trigger the prints because the 
# what is using @decorator is being called


# correct way
# create an inner funtion, put the actions in it, and return the
# inner object
def make_bold(func):
    def inner():
        print('<b>')
        func()
        print('</b>')
    return inner # return the object of inner

@make_bold
def print_name():
    print('Bryan Cairns')

print_name()


# Decorator with defined number of params

def num_check(func):
    def check_int(n):
        if isinstance(n, int):
            if n == 0:
                print('Can not divide by zero')
                return False
            return True
        print(f'{n=} is not a number')
        return False
    def inner(x, y):
        if not check_int(x) or not check_int(y):
            return
        return func(x, y)
    return inner

@num_check
def divide(a, b):
    print(a/b)

divide(100, 3)
divide(100, 0)
divide(100, 'cat')


# Decorator with unknown number of params
# *args, **kwargs

def outline(func):
    def inner(*args, **kwargs):
        print('~'*20)
        func(*args, **kwargs)
        print('~'*20)
    return inner

def list_items(func):
    def inner(*args, **kwargs):
        func(*args, **kwargs)
        print(f'{args=}')
        print(f'{kwargs=}')
        for x in args:
            print(f'{x=}')
        for key, value in kwargs.items():
            print(f'{key=} {value=}')
    return inner
    

@outline
@list_items
def display(msg):
    print(msg)
    
display('hello world')


@outline
@list_items
def birthday(name='', age=0):
    print(f'Happy birthday {name} you are {age} years old')

birthday(name='Bryan', age=46)
birthday('Bryan', 46)
birthday('Bryan', age=46)
    
