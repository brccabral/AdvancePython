# skipping

for _ in range(5):
    print('Hello')

# Test class
from person import Person, Child

# Single underscore before the variable name
# internal use only, called a weak private
# we should not change values that starts with underscore
# even though we can. The underscore indicates that the variable
# was created to be private, but there is no private in Python
p = Person()
p.set_name('Bryan')
print(f'Weak private {p._name=}')
p._name = 'Nooo'
print(f'Weak private {p._name=}')


# Double underscore before the variable name
p = Person()
p.work()
# p.__think() # can't call double underscore from an instance
c = Child()
# c.test_double() # double underscore can't be used in inheritance


# Any count of underscore after the variable
# it is used to make possible to have variables with reserved words
class_ = Person()
print(f'{class_=}')


# Before and after underscore
p = Person()
p.__call__() # can be used, but not recommended