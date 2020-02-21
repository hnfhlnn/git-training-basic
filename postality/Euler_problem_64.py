import time
from math import sqrt

# time at the start of program execution
start = time.time()
batas=10000

def contf(n):
    mn = 0.0
    dn = 1.0
    a0 = int(sqrt(n))
    an = a0
    period = 0
    if a0 != sqrt(n):
        while an != 2*a0:
            mn = dn*an - mn
            dn = (n - mn**2)/dn
            an = int((a0 + mn)/dn)
            period += 1
    return period

jumlah=0
for i in range(0,batas+1):
    if contf(i) % 2==1:
        jumlah += 1

print('continued fractions with odd period is: '+str(jumlah))

# time at the end of program execution
end = time.time()
print("time to solve: "+str(end - start))