import time

start = time.perf_counter()
batas=1000

xlist=[]
    
for D in range(2,batas+1):
    for x in range(2,10**5):
        y = ((x**2-1)/D) 
        k = y**0.5
        if k==int(k): #testing if the square root is integer
            xlist.append(x)
            break

#print(xlist)

maksX=0
for i in range(0,len(xlist)):
    if maksX < xlist[i]:
        maksX=xlist[i]
print(maksX)

end = time.perf_counter()
print("Time to solve:",end-start)
