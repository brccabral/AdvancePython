import json
import os.path
from collections import defaultdict

class Inventory:
    pets = defaultdict(int)
    def __init__(self):
        self.load()
    
    def add(self, key, qty):
        self.pets[key] += qty
        print(f'Added {qty} {key}: total = {self.pets[key]}')
    
    def remove(self, key, qty):
        self.pets[key] -= qty
        if self.pets[key] < 0:
            self.pets[key] = 0
        print(f'Removed {qty} {key}: total = {self.pets[key]}')
    
    def display(self):
        for key, value in self.pets.items():
            print(f'{key=} = {value=}')
    
    def save(self):
        print('Saving inventory')
        with open('inventory.txt', 'w') as f:
            json.dump(self.pets, f)
        print('Saved!')
    
    def load(self):
        print('Loading inventory')
        if not os.path.exists('inventory.txt'):
            print('Skipping, nothing to load')
            return
        with open('inventory.txt', 'r') as f:
            self.pets.update(json.load(f))
        print('Loaded!')

def test():
    i = Inventory()
    i.add('key', 4)
    print(i.pets)
    i.add('key', 7)
    print(i.pets)
    i.remove('key', 3)
    print(i.pets)
    i.remove('key', 3)
    print(i.pets)
    i.remove('key', 3)
    print(i.pets)
    i.remove('key', 3)
    print(i.pets)
    i.remove('key', 3)
    print(i.pets)
    i.remove('key', 3)
    print(i.pets)

def main():
    inv = Inventory()
    while True:
        action = input('Actions: add, remove, list, save, exit: ')
        if action == 'exit':
            break
        elif action == 'add' or action == 'remove':
            key = input('Enter an animal: ')
            qty = int(input('Enter an qty: '))
            if action == 'add':
                inv.add(key, qty)
            if action == 'remove':
                inv.remove(key, qty)
        elif action == 'list':
            inv.display()
        elif action == 'save':
            inv.save()
        

if __name__ == "__main__":
    main()