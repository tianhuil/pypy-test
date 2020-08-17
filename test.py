# mostly from https://blog.paperspace.com/getting-started-with-pypy/

import time

N = int(1e6)
nums = range(N)
sum = 0

t1 = time.time()
for k in nums:
    sum = sum + k
t2 = time.time()

print("Sum of {} numbers is : ".format(N), sum)
t = t2 - t1
print("Elapsed time is : ", t, " seconds")
