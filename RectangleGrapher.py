import matplotlib.pyplot as plt
import numpy as np
from bisect import bisect


test = "vacuum"

####################### Rect adaptive ###################################
solcost = [[]]
time = [[]]
firstpasscompleted = True
with open(test + "_results.txt") as infile:
    linenumber = 0
    for line in infile:            #Iterate each line
        entrynumber = 0
        currentline = line.split(",")
        sol = True

        if firstpasscompleted == True:
            firstpasscompleted = False
        else:
            solcost.append([])
            time.append([])

        for entry in currentline:
            if sol:
                solcost[linenumber].append( eval(entry) )
                sol = False
            else:
                time[linenumber].append( float(entry.replace("\n", "")) )
                sol = True
            entrynumber = entrynumber + 1
        linenumber = linenumber + 1


####################### Rect 1 ###################################
solcost1 = [[]]
time1 = [[]]
firstpasscompleted = True
with open(test + "_results1.txt") as infile:
    linenumber = 0
    for line in infile:            #Iterate each line
        entrynumber = 0
        currentline = line.split(",")
        sol = True

        if firstpasscompleted == True:
            firstpasscompleted = False
        else:
            solcost1.append([])
            time1.append([])

        for entry in currentline:
            if sol:
                solcost1[linenumber].append( eval(entry) )
                sol = False
            else:
                time1[linenumber].append( float(entry.replace("\n", "")) )
                sol = True
            entrynumber = entrynumber + 1
        linenumber = linenumber + 1



####################### Rect 500 ###################################
solcost500 = [[]]
time500= [[]]
firstpasscompleted = True
with open(test + "_results500.txt") as infile:
    linenumber = 0
    for line in infile:            #Iterate each line
        entrynumber = 0
        currentline = line.split(",")
        sol = True

        if firstpasscompleted == True:
            firstpasscompleted = False
        else:
            solcost500.append([])
            time500.append([])

        for entry in currentline:
            if sol:
                solcost500[linenumber].append( eval(entry) )
                sol = False
            else:
                time500[linenumber].append( float(entry.replace("\n", "")) )
                sol = True
            entrynumber = entrynumber + 1
        linenumber = linenumber + 1


####################### Rect combined ###################################
solcostcombined = [[]]
timecombined= [[]]
firstpasscompleted = True
with open(test + "_resultscombined.txt") as infile:
    linenumber = 0
    for line in infile:            #Iterate each line
        entrynumber = 0
        currentline = line.split(",")
        sol = True

        if firstpasscompleted == True:
            firstpasscompleted = False
        else:
            solcostcombined.append([])
            timecombined.append([])

        for entry in currentline:
            if sol:
                solcostcombined[linenumber].append( eval(entry) )
                sol = False
            else:
                timecombined[linenumber].append( float(entry.replace("\n", "")) )
                sol = True
            entrynumber = entrynumber + 1
        linenumber = linenumber + 1



####################### Rect 500 once then rect 1 ###################################
solcostONCE = [[]]
timeONCE= [[]]
firstpasscompleted = True
with open(test + "_resultsONCE.txt") as infile:
    linenumber = 0
    for line in infile:            #Iterate each line
        entrynumber = 0
        currentline = line.split(",")
        sol = True

        if firstpasscompleted == True:
            firstpasscompleted = False
        else:
            solcostONCE.append([])
            timeONCE.append([])

        for entry in currentline:
            if sol:
                solcostONCE[linenumber].append( eval(entry) )
                sol = False
            else:
                timeONCE[linenumber].append( float(entry.replace("\n", "")) )
                sol = True
            entrynumber = entrynumber + 1
        linenumber = linenumber + 1


maxval = max(max(solcost, key=max))
maxval1 = max(max(solcost1, key=max))
maxval500 = max(max(solcost500, key=max))
maxvalONCE = max(max(solcostONCE, key=max))
overall_max_val = max(maxval, maxval1, maxval500, maxvalONCE)

minval = min(min(solcost, key=min))
minval1 = min(min(solcost1, key=min))
minval500 = min(min(solcost500, key=min))
minvalONCE = min(min(solcostONCE, key=min))
overall_min_val = min(minval, minval1, minval500, minvalONCE)

maxtime = max(max(time, key=max))
maxtime1 = max(max(time1, key=max))
maxtime500 = max(max(time500, key=max))
maxtimeONCE = max(max(timeONCE, key=max))
overall_max_time = max(maxtime, maxtime1, maxtime500, maxtimeONCE)

mintime = min(min(time, key=min))
mintime1 = min(min(time1, key=min))
mintime500 = min(min(time500, key=min))
mintimeONCE = min(min(timeONCE, key=min))
overall_min_time = min(mintime,mintime1,mintime500,mintimeONCE)


print(overall_max_val)
print(overall_min_val)
print(overall_max_time)
print(overall_min_time)


timerange = np.linspace(mintime/2,maxtime*4,50000)
quality = [0]*len(timerange)
quality1 = [0]*len(timerange)
quality500 = [0]*len(timerange)
qualitycombined = [0]*len(timerange)
qualityONCE = [0]*len(timerange)


################################## adapt ##########################################
for i in range(len(time)):
    index = 0
    for h in range(len(timerange)):
        if index == len(time[i]):
            quality[h] += minval / solcost[i][index-1]
        elif timerange[h] <= time[i][index] and index == 0:
            quality[h] += 0
        elif timerange[h] <= time[i][index]:
            quality[h] += minval / solcost[i][index]
        else:
            quality[h] += minval / solcost[i][index]
            index = index + 1

for i in range(len(quality)):
    quality[i] = quality[i] / len(time)

# for i in range(len(quality)):
#     if quality[i] == 0:
#         quality[i] = np.nan

################################## 1 ##########################################
for i in range(len(time1)):
    index = 0
    for h in range(len(timerange)):
        if index == len(time1[i]):
            quality1[h] += minval / solcost1[i][index-1]
        elif timerange[h] <= time1[i][index] and index == 0:
            quality1[h] += 0
        elif timerange[h] <= time1[i][index]:
            quality1[h] += minval / solcost1[i][index]
        else:
            quality1[h] += minval / solcost1[i][index]
            index = index + 1

for i in range(len(quality1)):
    quality1[i] = quality1[i] / len(time1)

# for i in range(len(quality1)):
#     if quality1[i] == 0:
#         quality1[i] = np.nan


################################## 500 ##########################################
for i in range(len(time500)):
    index = 0
    for h in range(len(timerange)):
        if index == len(time500[i]):
            quality500[h] += minval / solcost500[i][index-1]
        elif timerange[h] <= time500[i][index] and index == 0:
            quality500[h] += 0
        elif timerange[h] <= time500[i][index]:
            quality500[h] += minval / solcost500[i][index]
        else:
            quality500[h] += minval / solcost500[i][index]
            index = index + 1

for i in range(len(quality500)):
    quality500[i] = quality500[i] / len(time500)

# for i in range(len(quality500)):
#     if quality500[i] == 0:
#         quality500[i] = np.nan


################################## combined ##########################################
for i in range(len(timecombined)):
    index = 0
    for h in range(len(timerange)):
        if index == len(timecombined[i]):
            qualitycombined[h] += minval / solcostcombined[i][index-1]
        elif timerange[h] <= timecombined[i][index] and index == 0:
            qualitycombined[h] += 0
        elif timerange[h] <= timecombined[i][index]:
            qualitycombined[h] += minval / solcostcombined[i][index]
        else:
            qualitycombined[h] += minval / solcostcombined[i][index]
            index = index + 1

for i in range(len(qualitycombined)):
    qualitycombined[i] = qualitycombined[i] / len(timecombined)

# for i in range(len(qualitycombined)):
#     if qualitycombined[i] == 0:
#         qualitycombined[i] = np.nan


################################## once ##########################################
for i in range(len(timeONCE)):
    index = 0
    for h in range(len(timerange)):
        if index == len(timeONCE[i]):
            qualityONCE[h] += minval / solcostONCE[i][index-1]
        elif timerange[h] <= timeONCE[i][index] and index == 0:
            qualityONCE[h] += 0
        elif timerange[h] <= timeONCE[i][index]:
            qualityONCE[h] += minval / solcostONCE[i][index]
        else:
            qualityONCE[h] += minval / solcostONCE[i][index]
            index = index + 1

for i in range(len(qualityONCE)):
    qualityONCE[i] = qualityONCE[i] / len(timeONCE)

# for i in range(len(qualitycombined)):
#     if qualitycombined[i] == 0:
#         qualitycombined[i] = np.nan


xpoints = np.array(timerange)
ypoints = np.array(quality)
ypoints1 = np.array(quality1)
ypoints500 = np.array(quality500)
ypointscombined = np.array(qualitycombined)
ypointsONCE = np.array(qualityONCE)

plt.xscale("log")
plt.xlabel("Time (seconds)")
plt.ylabel("Average Quality")
plt.title(test)
plt.plot(xpoints, ypoints, label="adaptive")
#plt.plot(xpoints, ypoints1, label="Rect(1)")
#plt.plot(xpoints, ypoints500, label="Rect(500)")
plt.plot(xpoints, ypointscombined, label="Rectangle Average")
plt.plot(xpoints, ypointsONCE, label="Rectangle 500 once")
plt.legend()
plt.show()