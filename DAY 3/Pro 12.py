#To print sum of odd numbers in a list
L,M = list(map(int,input().split()))
s = 0
for i in range (L,M+1):
    if i%2!=0:
        s+=i
print(s)


'''1 4
4'''


n,m = list(map(int,input().split()))
l = [i for i in range (n,m+1) if i%2!=0]
print(sum(l))
