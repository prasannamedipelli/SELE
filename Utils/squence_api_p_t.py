import threading
import requests
import time
urls = [
    "https://httpbin.org/delay/2",
    "https://httpbin.org/delay/2",
    "https://httpbin.org/delay/2"
]



threads = []
start =time.time()
def hit_api(url):
    response = requests.get(url)
    print(response.status_code)
    
for url in urls:
    t=threading.Thread(target=hit_api, args=(url,))
    threads.append(t)
    t.start()
for t in threads:
    t.join()
    
end = time.time()

print("Total time to take complete program ", end - start)
    