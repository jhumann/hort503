import numpy as np
import random

#random_array =np.random.normal(size=5)
#print(random_array)
for i in range(0,20):
    for x in range(1):
        x = random.randint(0,30)
    for y in range(1):
        y = random.randint(0,80)
    for z in range(1):
        z = random.randint(0,1)
    print(x, y, z)
