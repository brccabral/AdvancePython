import time
from threading import Timer

def display(msg):
    print(f'{msg} {time.strftime("%H:%M:%S")}')

def run_once():
    display('Run once:')
    # Timer(5 -> wait 5 seconds before executing the function,
    #   display -> function to be executed,
    #   [args] -> arguments passed to the function)
    t = Timer(5, display, ['Timeout'])
    t.start()

run_once()
# done is printed before Timeout because Timer has the 5 seconds start delay
print(f'done') 


# Interval timer

class RepeatTimer(Timer):
    # Timer.start() calls run()
    def run(self: Timer):
        # this run() will loop until the cancel() function below is called
        # self.interval = 1 (below)
        # self.function = display
        # self.args = ['Repeating']
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)
        print('Done')

timer = RepeatTimer(1, display, ['Repeating'])
timer.start()

print('threading started')
# the main thread is going to sleep, not the timers
# if comment this sleep(), the cancel() below will be called immediately
# and no "Repeating" message will appear
time.sleep(10)
print('threading finishing')

timer.cancel()
