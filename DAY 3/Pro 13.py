#To print the su1
#341
#11m of odd composite (not prime) numbers in a given range
def composite(n,l):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
        print("done",c)
        if c > 2:
            l.append(i)
       
a,b=int(input()),int(input())
l=[]
for i in range(a,b+1):
    if i%2!=0:
        print(i)
        flag=composite(i,l)
        if flag==1:
            l.append(i)
print(sum(l))
print(l)
            
        
    
