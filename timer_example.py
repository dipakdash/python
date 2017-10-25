from threading import Timer
import time

t = None
run = True

def hello():
    print "hello, world"
    if run:
        t = Timer(1.0, hello)
        t.start()


t = Timer(1.0, hello)
t.start() # after 30 seconds, "hello, world" will be printed
print "Timer enqueued"
print "Timer stated.. Will call in 10 sec"
print "Will stop the program in 20 sec."
print "\n\n"

time.sleep(20)
run = False
print "Timer stopped. Sleeping for 5 sec"
time.sleep(5)
print "Program exit."
