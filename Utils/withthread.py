import threading
import time
def task(name):
    print(f"{name} started....")
    time.sleep(5)
    print(f"{name} completed ...")
    
start = time.time()

t1= threading.Thread(target=task, args=("Booking Ticket...",))
t2 =threading.Thread(target=task, args=("Printing Ticket...",))
t3 = threading.Thread(target=task, args=("Cancelling Ticket...",))

t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()

end = time.time()

print ("Total time : ", end - start)