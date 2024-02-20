#To check given num is armstrong or not?
n = int(input())
m= n
rev = 0
for i in range(n):
    if n>0:
        digit= n%10
        rev = rev+digit**3
        n//=10
if rev == m:
    print("Armstrong")
else:
    print("Not Armstrong")

'''n = int(input())
m = n
rev=0
while n > 0:
    digit = n%10
    rev = rev+digit**3
    n//=10
if rev == m:
    print("Armstrong")
else:
    print("Not Armstrong")'''
    
        
