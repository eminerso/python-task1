import math
import random
lis=[]
sqrlis=[]
def poncik():
   for x in range(0,5):
    lis.append(random.randrange(20,50))
   for j in lis:
     if j %2==0:
       sqrlis.append(f"{j} nin kvadrati {math.pow(j,2)}")
       
poncik()           
for c in sqrlis:
  print(c)


