from multiprocessing import Process 
import time

def calculate():
    total = 0
    for i in range(10**7):
        total += i * i
        print("Calculation compleeted")
        
if __name__ == "__main__":
     
    start = time.time()

    processes = []

    for _ in range(4):
        p = Process(target=calculate)
        processes.append(p)
        p.start()
    
    for p in processes:
        p.join()
    end = time.time()
 
    print("Execution time  : ", round( end -  start , 2 ), "seconds")   