"""
Checking delay for sleep function
"""
import time

time_list = []



def sleep(duration, get_now=time.perf_counter):
    now = get_now()
    end = now + duration
    while now < end:
        now = get_now()


def measure_time(func):
    def wrapper(*arg):
        t = time.time()
        res = func(*arg)
        return time.time() - t #seconds

    return wrapper


@measure_time
def my_function(n):
    time.sleep(n) # seconds


def check_delay(sleep_duration):
    global time_list
    

    for x in range(10):
        time_list.append((my_function(sleep_duration) - sleep_duration) *1000) # difference in milli seconds returned from wrapper

    print(time_list)
    average_delay = sum(time_list) / len(time_list)

    print(f"""
    Times in milli seconds:
    Sleep duration {sleep_duration *1000}
    
    All the delays: {time_list}
    Highest delay: {max(time_list)} milliseconds
    Lowest delay: {min(time_list)} milliseconds
    Average delay: {average_delay} milliseconds
    Average inaccuracy: {(round(average_delay / (sleep_duration * 1000), 3)) * 100} %
    """)
    time_list = []


check_delay(1e-05)
check_delay(1e-04)
check_delay(1e-03)
check_delay(1e-02)
check_delay(0.1)
check_delay(1)