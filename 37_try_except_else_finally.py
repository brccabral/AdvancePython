# simple decorator
def outline(func):
    def inner(*args, **kwargs):
        print('~'*20)
        print(f'Function: {func.__name__}')
        func(*args, **kwargs)
        print('~'*20)
    return inner

@outline
def test_one(x, y):
    try:
        z = x /y
        print(f'{z=}')
    except Exception as e:
        print(f'Something bad happened {x=}, {y=}')
    finally:
        # doesn't matter what happens, this part will
        # be called
        # can be used to clean up, like close a file/connection
        print('Complete')

test_one(5, 0)
test_one(5, 'cat')
test_one(5, 2)

# usign assert
@outline
def test_two(x, y):
    try:
        assert(x > 0)
        assert(y > 0)
    except AssertionError as e:
        # specific type of error from the exception class
        print(f'Failed to assert {x=}, {y=}')
    except TypeError as e:
        print(f'Wrong type {x=}, {y=}')
    except Exception as e:
        print(f'Something bad happened {x=}, {y=}, issue {e=}')
    else:
        # this is executed if there was no exception in try block
        z = x /y
        print(f'{z=}')
    finally:
        # doesn't matter what happens, this part will
        # be called
        # can be used to clean up, like close a file/connection
        print('Complete')

test_two(5, 0) # will fail the assert
test_two(5, 'cat') # will fail because can't compare int > str
test_two(5, 2)




# user defined exceptions and raising
class CatError(RuntimeError):
    def __init__(self, *args):
        super().__init__()
        self.args = args

@outline
def test_cats(qty):
    try:
        if not isinstance(qty, int):
            # to raise, the raised class needs to be subclass of RuntimeError
            raise TypeError(f'Must be int {qty=}')
        if qty < 9:
            raise CatError(f'Must own more than 9 cats {qty=}')
        print(f'You own {qty} cats')
    except Exception as e:
        print(f'Opps: {e.args=}')
    finally:
        print('Complete')

test_cats('abc')
test_cats(3)
test_cats(12.3)
test_cats(11)