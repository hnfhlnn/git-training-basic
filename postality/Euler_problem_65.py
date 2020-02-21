import time
import math
import numpy as np
from fractions import Fraction
from decimal import Decimal

# time at the start of program execution
start = time.time()
eksponen=math.exp(1)
batas=100
terms=[]
termsC=[]

#continued fraction
terms = [2,]
i=1
kurang=batas%3
print(kurang)
sampai=batas-kurang-3
while len(terms) < sampai:
    terms.extend([1, 2*i, 1])
    i += 1
if kurang==0:
    terms.extend([1, 2*i])
elif kurang==1:
    terms.extend([1, 2*i, 1])
#print(terms)

# sum of digits in the numerator
list_hasil=[]
init=Fraction(0)
pembagi=terms[batas-1]
con=int(eksponen)
for j in range(2,batas+1):  
    hitung=Fraction(1/(init+Fraction(pembagi)))
    init=terms[batas-j]
    pembagi=hitung
hitung=Fraction(con)+hitung

hasil=str(Fraction(hitung).numerator)
jumlah=0
for i in hasil:
    jumlah=jumlah+int(i)
    
print("the result is: "+str(jumlah))

end = time.time()
print("time to solve: "+str(end - start))