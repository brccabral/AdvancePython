import logging
"""
DEBUG
INFO
WARNING
ERROR
CRITICAL
"""
def test():
    print('~'*20)
    level = logging.getLevelName(logging.getLogger().getEffectiveLevel())
    print(f'Log level: {level=}')
    logging.debug('debug message here')
    logging.info('info message here')
    logging.warning('warning message here')
    logging.error('error message here')
    logging.critical('critical message here')
    print('-'*20)


# get and set log level

rootlog = logging.getLogger()
print(f'Level {logging.getLevelName(rootlog.getEffectiveLevel())}')
test()

rootlog.setLevel(logging.DEBUG)
test()

rootlog.setLevel(logging.CRITICAL)
test()

rootlog.setLevel(logging.WARNING)
test()


# Log to file
# basicConfig will not work if logger is already configured/used
# above, root logger is already used
# below, we are creating a new logger as a file
# logging.basicConfig(filename='app_101.log', filemode='w', format='%(levelname)s:%(message)s', level=logging.DEBUG)
# logging.debug('hello')

handler = logging.FileHandler('app_101.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
rootlog.addHandler(handler)
rootlog.setLevel(logging.DEBUG)
# the messages get printed in terminal and in file
# file is appending new messages each run of the script
rootlog.debug('debug msg')
test()