#write a python program to check given number is prime number or no?
'''n=int(input())
c=0
for i in range(1,n+1):
    print("Prime")
else:
    print("Not Prime")'''
#without using count
'''n=int(input())
for i in range(2,n):
    if n%i==0:
        print("Not a Prime")
        break
else:
    print("Prime")'''

#half iterations
'''n=int(input())
for i in range(2,(n//2)+1):
    if n%i==0:
        print("Not a Prime")
        break
else:
    print("Prime")'''

#sqrt-1/2=0.5
'''n=int(input())
for i in range(2,(n**0.5)+1):
    if n%i==0:
        print("Not a Prime")
        break
else:
    print("Prime")'''

n = int(input())
i = 2
while i<(n**0.5)+1:
    if n%i==0:
        print("Not a Prime")
        break
    i+=1
else:
    print("Prime")
        


        
        
    
    
