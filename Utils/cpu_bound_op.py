import time

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** .05)+1):
        if n % i == 0:
            return False
    return True

start = time.time()

count = 0
for num in range(1, 100000):
    if is_prime(num):
        count += 1
end = time.time()

print("Total prime number ", count)

print("Execution  time : ", round(end - start, 2), "seconds")