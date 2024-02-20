'''np,ns=map(int,input().split())
c=np*ns
if c%4==0:
    p = c//4
else:
    p = (c//4)+1
print(p)'''

import math
np,ns=map(int,input().split())
c = np*ns
p = math.ceil(c/4)
print(p)

