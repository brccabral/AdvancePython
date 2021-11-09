import os

stats = dict(path='', folders=0, files=0, links=0, size=0)

def get_input():
    global stats
    ret = os.path.abspath(input('Enter a folder path: '))

    if not os.path.exists(ret):
        print(f'Sorry path does not exist')
        exit(1)
    if not os.path.isdir(ret):
        print(f'Sorry path is not directory')
        exit(2)
    
    stats['path'] = ret

def scan(path):
    global stats
    print(f'Scanning {path}')

    for root, dirs, files in os.walk(path, onerror=None, followlinks=False):
        stats['folders'] += len(dirs)
        stats['files'] += len(dirs)
        for name in files:
            fullname = os.path.join(root, name)
            size = os.path.getsize(fullname)
            stats['size'] += size

def display():
    global stats
    print(f'Results')
    for key, value in stats.items():
        print(f'{key=} {value=}')

def main():
    global stats
    get_input()
    scan(stats['path'])
    display()

if __name__ == "__main__":
    main()
    