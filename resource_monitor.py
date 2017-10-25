
import os
import sys
import time
import subprocess
from threading import Timer

class ResourceMonitor(object):
    # Start monitoring all resources.
    exec_str = None
    n = 1
    # RAM information (unit=kb) in a list
    # Index 0: total RAM
    # Index 1: used RAM
    # Index 2: free RAM

    def __init__(self, interval):
        self.interval = interval
        self._timer = None
        self.is_running = False
        f = open("CPU_Use.txt", "w")
        f.close()
        f = open("IO_usage.txt", "w")
        f.close()

    def getRAMinfo(self):
        #self.exec_str = 'free'
        #_process = subprocess.Popen (self.exec_str,
        #                                shell=True,
        #                                stdout=subprocess.PIPE,
        #                                stdin=subprocess.PIPE,
        #                                stderr=subprocess.PIPE,
        #                                creationflags=flags,
        #                                env=os.environ
        #                                )
        p = os.popen('free')
        i = 0
        while 1:
            i = i + 1
            line = p.readline()
            if i==2:
                return(line.split()[1:4])

    # Return % of CPU used by user as a character string
    def getCPUuse(self):
        return(str(os.popen("top -n1 | awk '/Cpu\(s\):/ {print $2}'").readline()))
        #readline().strip(\)))
        time.sleep(3)

    def Start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self.getRAMinfo())
            self._timer.start()
            self.is_running = True
        ram = ("RAM info: %s %s") % (self.getRAMinfo(), "\n")
        #print ("CPU use: %s %s") % (self.getCPUuse(), "\n")

        

    # Stop monitoring all resources.
    def Stop(self):
        print("stop")

    # Get the latest value (moving average) for the statistic 'stat_name'.
    def GetStatistic(self, stat_name):
        print stat_name

if __name__ == "__main__":
    interval = 10
    obj = ResourceMonitor(interval)
    obj.Start()
    obj.Stop()
    obj.GetStatistic("stat_name")
