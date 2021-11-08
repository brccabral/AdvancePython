class Person:
    # single underscore before
    # weak private
    _name = 'No name'
    def set_name(self, name):
        self._name = name
        print(f'Name set to {self._name=}')
    
    # double underscore before
    # Strong private
    def __think(self):
        print('Thinking to myself')
    def work(self):
        self.__think()
    
    # before and after underscore
    # can be used, but not recommended
    def __init__(self):
        print('Constructor')
    
    def __call__(self):
        print('call someone')
    

class Child(Person):
    def test_double(self):
        self.__think(self) # double underscore can't be used in inheritance
    
    
    