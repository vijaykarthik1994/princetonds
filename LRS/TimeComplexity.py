import  time as mytime
class MyChecker:
    def PerformFunction(self, n):
        t1 = mytime.perf_counter()
        for i in range(n):
            mytime.sleep(1)
        t2 = mytime.perf_counter()
        print(t2 - t1)


mynumbs = int(input("Enter a length"))
mych = MyChecker()
mych.PerformFunction(mynumbs)
