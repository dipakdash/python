import os
import time
from threading import Timer
from time import sleep

class ResourceMonitor(object):
    def __init__(self, interval):
        self.interval = interval
        self._timer = None
        self.run = True

    def getRAMinfo(self):

        p = os.popen('free')
        i = 0
        while 1:
            i = i + 1
            line = p.readline()
            if i==2:
                print (line.split()[1:4])
                break;
        if self.run:
            t = Timer(self.interval, self.getRAMinfo)
            t.start()

    def Start(self, func):
        t = Timer(1.0, func)
        t.start() # after 1 seconds, func() will be called

    def Stop(self):
        self.run = False

    # Get the latest value (moving average) for the statistic 'stat_name'.
    def GetStatistic(self, stat_name):
        print stat_name

if __name__ == "__main__":
    interval = 1
    obj = ResourceMonitor(interval)
    obj.Start(obj.getRAMinfo)
    sleep(5)
    obj.Stop()
    #obj.GetStatistic("stat_name")
