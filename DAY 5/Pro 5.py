l,d =map(int,input().split())
n = list(map(int,input().split()))
flag = 0
for i in n:
    for j in n:
        if (i-j) == d:
            flag = 1
x = True if flag == 1 else False
print(x)

'''5 60
1 20 40 100 80            #1-20,1-40,1-100,1-80,20-1,20-40.....
True'''

    
