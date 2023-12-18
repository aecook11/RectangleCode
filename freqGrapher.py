import matplotlib.pyplot as plt
import numpy as np
from bisect import bisect



####################### Rect adaptive ###################################
depth = []
errors = []
expansions = []

with open("frequency.txt") as infile:
    linenumber = 0
    for line in infile:            #Iterate each line
        currentline = line.split(" ")
        iter = 0
        for entry in currentline:
            if iter == 0:
                depth.append(int(entry))
                iter = iter+1
            elif iter == 1:
                errors.append(int(entry))
                iter = iter + 1
            elif iter == 2:
                expansions.append(int(entry))
                iter = 0

print(depth)
print(errors)
print(expansions)

#plt.xscale("log")
plt.xlabel("depth")
plt.ylabel("expansions/errors")
plt.title("Crossover Frequency")
plt.plot(depth, errors, label="errors")
plt.plot(depth, expansions, label="expansions")
plt.legend()
plt.show()