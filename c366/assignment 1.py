import random
import math


tar = [-1,-1,-1,-1,-1,-1]
est_1 = 0
est_2 = 0
est_8 = 0
u= 0
i=0
a_1= 1
a_2= 1/2
a_8= 1/8
next =0
#clist = [0,0,0]
sum = [0,0,0]

while(i<10000):
    
    next = random.normalvariate(u, 1)
    u+= random.normalvariate(0, 1)
    sum[0]+=abs(est_1-next)
    sum[1]+=abs(est_2-next)
    sum[2]+=abs(est_8-next)
    #print(est_1,est_2,est_8,next)

    est_1 = est_1 + a_1*(next-est_1)
    est_2 = est_2 + a_2*(next-est_2)
    est_8 = est_8 + a_8*(next-est_8)

    i+=1

#if (abs(est_1-next)>abs(est_2-next)):
  #  if (abs(est_2-next)>abs(est_8-next)):
  #      clist[2] = clist[2]+1
   # else:
   #     clist[1] = clist[1]+1
  #  else:
   #     if (abs(est_1-next)>abs(est_8-next)):
     #       clist[2] = clist[2]+1
   #     else:
     #       clist[0] = clist[0]+1

print(sum)
    
    
