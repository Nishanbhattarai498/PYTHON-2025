import threading
import time

def eat_breakfast():
    time.sleep(3)
    print("you eat breakfast")


def drink_cofee():
    time.sleep(4)
    print("you drink coffee")


def study():
    time.sleep(5)
    print("you finished studying")

x=threading.Thread(target=eat_breakfast,args=())
x.start()


y=threading.Thread(target=drink_cofee,args=())
y.start()

z=threading.Thread(target=study,args=())
z.start()

x.join()
y.join()
z.join()

# eat_breakfast()
# drink_cofee()
# study()



print(threading.enumerate())
print(threading.active_count())
print(time.perf_counter())  