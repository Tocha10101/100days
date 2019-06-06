import time

def calc_sleep(i):
    print(f"{i // 600}{i // 60 % 10}:{i % 60 // 10}{i % 10}")
    time.sleep(1)

def pomodoro_time():
    for i in range(60 * 25, 0, -1):
        calc_sleep(i)

def short_break_time():
    for i in range(60 * 5, 0, -1):
        calc_sleep(i)
    
def long_break_time():
    for i in range(60 * 10, 0, -1):
        calc_sleep(i)
        
mode = input("Enter please the mode (p, sb, lb): ")

if mode == 'p':
    pomodoro_time()
elif mode == 'sb':
    short_break_time()
elif mode == 'lb':
    long_break_time()
