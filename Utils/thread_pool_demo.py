from concurrent.futures import ThreadPoolExecutor

import time

def task(num):
    print(f"Task {num}  started..")
    
    time.sleep(5)
    
    print(f"Task {num} completed..")
    
    return f"Result of task {num}" 
def main():
        start= time.time()
    
        with ThreadPoolExecutor(max_workers=5) as executor:
            results = executor.map(task,[1,2,3,4,5])
            #print the returned result
            for result in results:
                print(result)
        end = time.time()
        
        print("Total execution time ", round(end - start,2),"seconds")

#create main method as entry point
if __name__=="__main__":
    main()