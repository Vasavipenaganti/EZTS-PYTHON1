#To check given number strong number r not
#Strong number = sum of the factorial of individual digits = 145
'''def strongnum(n):
    x,sum =n,0
    while n > 0:
        digit = n%10
        fact = 1
        for i in range(1,digit+1):
            fact*=i
        sum+=fact
        n//=10
        if sum == x:
        return "Strong Number"           #print("Strong Number")
    else:
        return "Not a Strong Number" #print("Not a strong number")
n = int(input())
print(strongnum(n))                          #strongnum(n)'''

def strongnum(n,m):
    for i in range(n,m+1):
        x,sum =i,0
        while i > 0:
            digit = i%10
            fact = 1
            for j in range(1,digit+1):
                fact*=j
            sum+=fact
            i//=10
        if sum == x:
            print(x)       
n,m = int(input()),int(input())
strongnum(n,m)                     
    
            
    
   
        
