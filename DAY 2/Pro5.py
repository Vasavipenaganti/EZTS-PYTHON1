#To check number is perfect number or  not?
#sum of the factors = same number  1+2+3=6,28
n = int(input())
c=0
for i in range(1,n):
    if n%i==0:
        c+=i
if c ==n:
    print("Perfect")
else:
    print("Not a Perfect")
        
