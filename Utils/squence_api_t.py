import requests
import time
urls = [
    "https://httpbin.org/delay/2",
    "https://httpbin.org/delay/2",
    "https://httpbin.org/delay/2"
]

start =time.time()
for url in urls:
    response = requests.get(url)
    print(response.status_code)
    
end =time.time()

print("Time taken to complete the program ", end - start)