myCount = [777, 888, 7, 555, 11]
for x in range(len(myCount)):
    steen1 = myCount[x]
    if x == len(myCount) - 1:
        altCount = 0 
    else:
        altCount = x + 1
    steen2 = myCount[altCount]
    SOM = steen1 + steen2
    print(SOM)     
     
