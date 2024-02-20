import threading
import random
import time

class MyClass(threading.Thread):

    def run(self):
        tid = threading.get_ident()
        s = random.randint(1, 5)
        print("[{0}] Sleeping for {1}".format(tid, s))
        time.sleep(s)
        print("[{0} ]I'm awake!".format(tid))

print("About to launch threads")

for i in range(5):z
    t = MyClass()
    t.start()
print("Done launching threads")


''' when you threading.enumerate to  see the live threads, it also returns the main thread that lanauched are additional threads
threading.enumerate() function returns all of the currently alive threads
join waits for threads to finish argument time to wait
'''
while len(threading.enumerate()) > 1:  # while there is still some live threads
    
    for t in threading.enumerate():
        if threading.current_thread() == t:
            continue

        t.join(0.1)
        if t.is_alive():
            print("join of thread {} failed".format(t.ident))
        else:
            print("join of {} succeeded; removing".format(t.ident))
print("All threads are done")