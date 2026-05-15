import time
def task(name):
    print(f"{name} started....")
    time.sleep(5)
    print(f"{name} completed ...")


start =time.time()

task("booking ticket..")
task("printing ticket..")
task("Cancelling ticket..")

end =time.time()
print ("Total time : ", end - start)
    