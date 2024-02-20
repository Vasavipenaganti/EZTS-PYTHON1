import math
nc,cd = map(int,input().split())
if cd >= nc:
    np = 0
else:
    c = nc-cd
    np=math.ceil(c/4)
print(np)
    


