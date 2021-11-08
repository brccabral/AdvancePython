from cat import Feline, Lion, Tiger

c = Feline('kitty')
print(c)
c.meow()

l = Lion('Leo')
print(l)
l.meow() # this method was inherited from Feline
l.roar()

t = Tiger()
print(t)
t.stalk() # prints "No name: stalking"
t.rename('Tony')
t.meow()
t.stalk() # prints "Tony: stalking"