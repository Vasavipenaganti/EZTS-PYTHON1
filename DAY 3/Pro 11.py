#To remove duplicate values in List
n = list(map(int,input().split()))
n1=[]
for i in n:
    if i not in n1:
         n1.append(i)
print(n1)
