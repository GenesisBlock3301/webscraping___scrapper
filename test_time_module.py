from time import sleep
from random import randint

from time import time
start_time = time()
requests = 0
for _ in range(5):
# A request would go here
    requests += 1
    sleep(randint(1,3))
    elapsed_time = time() - start_time
    # print(elapsed_time)
    print('Request: {}; Frequency: {} requests/s'.format(requests, requests/elapsed_time))
