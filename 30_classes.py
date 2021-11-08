# import cat
from cat import Cat

def test():
    b = Cat('KitKat', 1, 'tabby')
    c = Cat('Pthello', 6, 'black')
    b.description()
    c.description()
    print(b)
    print(c)

    c.meow()
    b.sleep()
    c.hungry()
    b.eat()

def main():
    test()

if __name__ == "__main__":
    x = Cat('test')
    print(x)
    # <cat.Cat object at 0x7f00880fef10>
    # 0x7f00880fef10 is the memory address
    main()