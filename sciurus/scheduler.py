'''
@uthor: saleem

Minimal Scheduler for running functions at set interval.
'''
import time

class scheduler:
    def __init__(self, h=0, m=0, s=0):
        self.h = h
        self.m = m
        self.s = s

    def runit(self, fn, *args):
        time_step = self.h*3600 + self.m*60 + self.s
        while True:
            starttime = time.time()
            fn(*args)
            exec_time = time.time()-starttime
            tlambda = int(exec_time)/time_step
            ttime = (tlambda+1)*time_step
            time.sleep(ttime - ((time.time()-starttime)%ttime))

if __name__ == "__main__":
    def fn(a, b):
        print a+b
        return
    ss = scheduler(s=3)
    ss.runit(fn, 1, 3)
